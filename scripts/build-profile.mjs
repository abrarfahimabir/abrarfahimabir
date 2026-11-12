#!/usr/bin/env node
// No npm install needed. Node 22+. Only public GitHub metadata is requested.
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const file = (p) => path.join(root, p);
const xml = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;' })[c]);
const dateLabel = (s) => new Intl.DateTimeFormat('en-GB', {
  day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC',
}).format(new Date(s));

async function api(route) {
  const headers = { Accept: 'application/vnd.github+json', 'User-Agent': 'abrar-profile', 'X-GitHub-Api-Version': '2022-11-28' };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      const res = await fetch(`https://api.github.com${route}`, { headers, signal: AbortSignal.timeout(20000) });
      if (!res.ok) throw new Error(`Public GitHub API returned HTTP ${res.status} for ${route}.`);
      return await res.json();
    } catch (err) {
      if (attempt === 2) throw err;
      await new Promise((resolve) => setTimeout(resolve, 1000 * (attempt + 1)));
    }
  }
}

function validateConfig(config) {
  if (!/^[a-z\d](?:[a-z\d-]{0,37}[a-z\d])?$/i.test(config.username ?? '')) {
    throw new Error('profile.config.json needs a valid GitHub username.');
  }
  if (!Array.isArray(config.activity?.exclude) || !config.activity.exclude.every((x) => typeof x === 'string')) {
    throw new Error('activity.exclude must be a list of repository names.');
  }
  for (const [key, max] of [['recentLimit', 5], ['languageLimit', 5]]) {
    if (!Number.isInteger(config.activity[key]) || config.activity[key] < 1 || config.activity[key] > max) {
      throw new Error(`activity.${key} must be an integer from 1 to ${max}.`);
    }
  }
}

async function collect(config) {
  let repos = [];
  for (let page = 1; ; page++) {
    const batch = await api(`/users/${config.username}/repos?type=owner&sort=pushed&per_page=100&page=${page}`);
    if (!Array.isArray(batch)) throw new Error('GitHub returned an unexpected repository list.');
    repos.push(...batch);
    if (batch.length < 100) break;
  }
  const exclude = new Set(config.activity.exclude.map((name) => name.toLowerCase()));
  const included = repos.filter((r) => !r.fork && !r.archived && !exclude.has(r.name.toLowerCase()) && r.size > 0);
  const bytes = {};
  // Keep requests sequential to respect GitHub's API limits.
  for (const repo of included) {
    const languages = await api(`/repos/${config.username}/${encodeURIComponent(repo.name)}/languages`);
    for (const [name, value] of Object.entries(languages)) {
      if (typeof value !== 'number' || value < 0 || !Number.isFinite(value)) throw new Error('Invalid language data.');
      bytes[name] = (bytes[name] ?? 0) + value;
    }
  }
  return {
    schemaVersion: 1,
    username: config.username,
    checkedOn: new Date().toISOString().slice(0, 10),
    scope: 'Non-fork, non-archived public repositories, excluding activity.exclude; language shares use GitHub code bytes, not proficiency.',
    excluded: config.activity.exclude,
    repositories: included.map((r) => ({ name: r.name, url: r.html_url, language: r.language, pushedAt: r.pushed_at })),
    languageBytes: Object.fromEntries(Object.entries(bytes).sort((a, b) => b[1] - a[1])),
  };
}

function validateSnapshot(data, config) {
  if (data.schemaVersion !== 1 || data.username !== config.username || !/^\d{4}-\d{2}-\d{2}$/.test(data.checkedOn)
      || !Number.isFinite(Date.parse(data.checkedOn)) || !Array.isArray(data.repositories)
      || !data.languageBytes || !Object.values(data.languageBytes).every((v) => typeof v === 'number' && v >= 0)) {
    throw new Error('Public-code snapshot is invalid or belongs to another username.');
  }
  for (const repo of data.repositories) {
    if (repo.url !== `https://github.com/${config.username}/${repo.name}` || !Number.isFinite(Date.parse(repo.pushedAt))) {
      throw new Error('Invalid repository URL or date in public-code snapshot.');
    }
  }
}

function mix(data, limit) {
  const entries = Object.entries(data.languageBytes).filter(([, n]) => n > 0).sort((a, b) => b[1] - a[1]);
  const selected = entries.slice(0, limit);
  if (entries.length > limit) selected.push(['Other', entries.slice(limit).reduce((sum, [, v]) => sum + v, 0)]);
  const total = selected.reduce((sum, [, n]) => sum + n, 0);
  const rows = selected.map(([name, bytes]) => ({ name, share: bytes / total, percent: Math.floor(bytes / total * 100) }));
  const missing = 100 - rows.reduce((sum, r) => sum + r.percent, 0);
  [...rows].sort((a, b) => (b.share * 100 - b.percent) - (a.share * 100 - a.percent))
    .slice(0, missing).forEach((r) => r.percent++);
  return rows;
}

const palette = { JavaScript: '#f0d771', TypeScript: '#72b8ef', Python: '#b8f780', CSS: '#b4a5ff', HTML: '#eea882', Other: '#74849e' };
function activitySvg(data, rows) {
  let x = 42;
  const bars = rows.map((r) => {
    const w = r.share * 1196;
    const rect = `<rect x="${x.toFixed(2)}" y="91" width="${w.toFixed(2)}" height="17" fill="${palette[r.name] ?? '#72dfee'}"/>`;
    x += w; return rect;
  }).join('\n');
  const labels = rows.map((r, i) => {
    const xx = 42 + i * (1196 / Math.max(1, rows.length));
    return `<circle cx="${xx}" cy="147" r="4" fill="${palette[r.name] ?? '#72dfee'}"/>
    <text x="${xx + 14}" y="152" font-size="15" fill="#edf3ff">${xml(r.name)} <tspan fill="#a1b0c8">${r.percent}%</tspan></text>`;
  }).join('\n');
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="222" viewBox="0 0 1280 222" role="img" aria-labelledby="title desc">
  <title id="title">Public code language mix</title><desc id="desc">${xml(rows.length ? rows.map((r) => `${r.name} ${r.percent}%`).join(', ') : 'No language data available')}. Code bytes, not proficiency. Checked ${xml(data.checkedOn)}.</desc>
  <defs><clipPath id="bar"><rect x="42" y="91" width="1196" height="17" rx="8.5"/></clipPath></defs>
  <rect x="1" y="1" width="1278" height="220" rx="20" fill="#0b1320" stroke="#243145"/>
  <g font-family="Arial, Helvetica, sans-serif">
    <text x="42" y="45" font-size="15" letter-spacing="2" fill="#b8f780">PUBLIC CODE / LANGUAGE MIX</text>
    <text x="1238" y="45" text-anchor="end" font-size="13" fill="#a1b0c8">${xml(dateLabel(data.checkedOn))} · UTC</text>
    <rect x="42" y="91" width="1196" height="17" rx="8.5" fill="#243145"/>
    <g clip-path="url(#bar)">${bars}</g>${labels}
    <text x="42" y="192" font-size="13" fill="#8b9cb6">${rows.length ? 'By code bytes across public repositories. Excludes forks, archived repos and this profile.' : 'No language data found in the selected public repositories.'}</text>
  </g>
</svg>\n`;
}

function block(data, rows, config) {
  const summary = rows.map((r) => `${r.name} ${r.percent}%`).join(' · ');
  const recent = [...data.repositories].sort((a, b) => new Date(b.pushedAt) - new Date(a.pushedAt)).slice(0, config.activity.recentLimit);
  const list = recent.map((r) => `- [${r.name.replace(/[\[\]\\]/g, '\\$&')}](${r.url}) · ${r.language ?? 'Code'} · ${dateLabel(r.pushedAt)}`).join('\n');
  return `<!-- ACTIVITY:START -->\n<img src="assets/activity.svg" width="100%" alt="Public code by language: ${xml(summary || 'no data')}. Code size, not proficiency.">\n\n<sub>${summary || 'No language data yet.'}</sub>\n\n**Recently pushed**\n\n${list || 'No matching public repositories yet.'}\n\n<sub>Public GitHub API · refreshed weekly · checked ${dateLabel(data.checkedOn)} (UTC). Repository push dates are separate from this snapshot date.</sub>\n<!-- ACTIVITY:END -->`;
}

async function main() {
  const config = JSON.parse(await readFile(file('profile.config.json'), 'utf8'));
  validateConfig(config);
  const readme = await readFile(file('README.md'), 'utf8');
  if ((readme.match(/<!-- ACTIVITY:START[^\n]*-->/g) ?? []).length !== 1
      || (readme.match(/<!-- ACTIVITY:END -->/g) ?? []).length !== 1) {
    throw new Error('README.md must contain exactly one ACTIVITY:START and one ACTIVITY:END marker.');
  }
  const pattern = /<!-- ACTIVITY:START[^\n]*-->[\s\S]*?<!-- ACTIVITY:END -->/;
  if (!pattern.test(readme)) throw new Error('Activity markers must appear in START then END order.');
  const offline = process.argv.includes('--offline');
  const snapshot = offline ? JSON.parse(await readFile(file('data/public-code.json'), 'utf8')) : await collect(config);
  validateSnapshot(snapshot, config);
  const rows = mix(snapshot, config.activity.languageLimit);
  // No file is written until all API requests and validation have succeeded.
  await mkdir(file('assets'), { recursive: true });
  await mkdir(file('data'), { recursive: true });
  await writeFile(file('assets/activity.svg'), activitySvg(snapshot, rows));
  await writeFile(file('README.md'), readme.replace(pattern, () => block(snapshot, rows, config)));
  if (!offline) await writeFile(file('data/public-code.json'), JSON.stringify(snapshot, null, 2) + '\n');
  console.log(`Updated ${snapshot.username}: ${snapshot.repositories.length} repositories, ${rows.length} language groups; ${offline ? 'bundled snapshot' : 'live public API'}.`);
}

main().catch((err) => { console.error(`Profile update failed: ${err.message}`); process.exitCode = 1; });

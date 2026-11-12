# Profile README সেটআপ গাইড

এই গাইড ধরে নিচ্ছে আপনি আগে কখনো GitHub profile README আপলোড করেননি। প্রতিটা ধাপ ক্রমানুসারে করুন। GitHub-এর বাটন আর মেনুর নাম ইংরেজিতেই রাখা হয়েছে, কারণ স্ক্রিনে আপনি ঠিক এই লেখাগুলোই দেখবেন।

---

## এই ফোল্ডারে কী আছে

| ফাইল বা ফোল্ডার | কাজ |
| --- | --- |
| `README.md` | আপনার profile পেজে যা দেখা যাবে |
| `SETUP.md` | এই গাইড |
| `profile.config.json` | নাম, role, subtitle আর tech stack এক জায়গায় রাখার ফাইল |
| `assets/` | banner, বাটন, tech chip আর language bar-এর ছবি (সব SVG) |
| `scripts/build-profile.mjs` | config থেকে ছবিগুলো আর README-র কিছু অংশ নতুন করে বানায় |
| `scripts/icons.json` | tech chip-এর লোগো (Simple Icons, CC0 লাইসেন্স) |
| `.github/workflows/update-profile.yml` | সপ্তাহে একবার নিজে নিজে ছবি আর activity আপডেট করে |

কোনো বাইরের ছবি-সার্ভিস ব্যবহার করা হয়নি। সব ছবি আপনার নিজের repository থেকেই দেখানো হয়, তাই অন্য কোনো সাইট বন্ধ থাকলেও profile ঠিক থাকবে।

---

## ধাপ ১: Profile repository তৈরি বা যাচাই করা

GitHub তখনই README-টা profile-এ দেখায় যখন:

- repository-র নাম হুবহু আপনার username: **`abrarfahimabir`**
- repository-টা **Public**
- repository-র একদম মূল জায়গায় (root-এ) `README.md` ফাইল আছে

**আপনার ক্ষেত্রে:** `abrarfahimabir/abrarfahimabir` repository আগে থেকেই আছে। তাই নতুন করে বানাতে হবে না, সরাসরি ধাপ ২-এ যান।

যদি কখনো repository-টা মুছে যায়, তাহলে নতুন বানাবেন এভাবে:

1. GitHub-এর উপরে ডানদিকে **+** চিহ্নে ক্লিক করে **New repository** বেছে নিন।
2. **Repository name** ঘরে লিখুন `abrarfahimabir` (বড় হাতের বা ছোট হাতের অক্ষর হুবহু মিলতে হবে)।
3. **Public** বেছে নিন।
4. **Add README** চালু করুন।
5. **Create repository** চাপুন।

---

## ধাপ ২: GitHub-এর ওয়েবসাইট দিয়ে ফাইল আপলোড করা

1. ব্রাউজারে খুলুন: https://github.com/abrarfahimabir/abrarfahimabir
2. ফাইল লিস্টের উপরে **Add file** চাপুন, তারপর **Upload files**।
3. কম্পিউটারের ফোল্ডার থেকে এগুলো টেনে এনে ব্রাউজারে ছেড়ে দিন:
   - `README.md`
   - `SETUP.md`
   - `profile.config.json`
   - `assets` ফোল্ডার (পুরো ফোল্ডারটাই টেনে আনুন)
   - `scripts` ফোল্ডার (পুরো ফোল্ডারটাই টেনে আনুন)

   Chrome, Edge বা Firefox-এ ফোল্ডার টেনে আনলে GitHub ভেতরের ফোল্ডার কাঠামো ঠিক রাখে।
4. নিচে **Commit changes** অংশে একটা ছোট বার্তা লিখুন, যেমন `New profile README`।
5. **Commit directly to the `main` branch** বেছে রেখে **Commit changes** চাপুন।

একই নামের পুরোনো ফাইল (যেমন `README.md` বা `assets/stack/react.svg`) থাকলে নতুনটা দিয়ে নিজে নিজেই বদলে যাবে।

### `.github` ফোল্ডারটা আলাদা করে যোগ করুন

নামের শুরুতে বিন্দু থাকায় `.github` ফোল্ডারটা Mac আর Windows দুটোতেই সাধারণত লুকানো থাকে, তাই টেনে আনার সময় অনেকে এটা মিস করেন। সবচেয়ে নিরাপদ উপায় হলো ফাইলটা হাতে তৈরি করা:

1. repository পেজে **Add file** চাপুন, তারপর **Create new file**।
2. নামের ঘরে হুবহু লিখুন: `.github/workflows/update-profile.yml`
   (`/` টাইপ করলেই GitHub নিজে থেকে ফোল্ডার বানিয়ে দেয়।)
3. আপনার কম্পিউটারের `.github/workflows/update-profile.yml` ফাইলটা যেকোনো text editor-এ খুলুন, পুরো লেখা কপি করে GitHub-এর বড় ঘরে পেস্ট করুন।
4. **Commit changes...** চাপুন, তারপর আবার **Commit changes**।

> লুকানো ফোল্ডার দেখতে চাইলে: Mac-এর Finder-এ `Cmd + Shift + .` চাপুন। Windows-এ File Explorer-এ **View** মেনু থেকে **Hidden items** চালু করুন।

---

## ধাপ ৩: পুরোনো ব্যানারের ফাইলগুলো মুছে ফেলা

আগের ভার্সনের এই ছয়টা ফাইল নতুন README-তে আর ব্যবহার হয় না:

```
assets/hero-dark.gif
assets/hero-light.gif
assets/hero-dark.png
assets/hero-light.png
assets/hero-dark.svg
assets/hero-light.svg
```

রেখে দিলে profile-এ কোনো ক্ষতি হবে না, তবে repository পরিষ্কার রাখতে মুছে ফেলাই ভালো। প্রতিটা ফাইলের জন্য:

1. `assets` ফোল্ডারে ঢুকে ফাইলটার নামে ক্লিক করুন।
2. ডানদিকে উপরে **...** (More file actions) চাপুন, তারপর **Delete file**।
3. **Commit changes...** চাপুন, তারপর আবার **Commit changes**।

---

## ধাপ ৪: ফোল্ডার কাঠামো ঠিক আছে কিনা দেখা

আপলোড শেষে repository-র মূল পেজে কাঠামোটা ঠিক এমন হওয়া উচিত:

```
abrarfahimabir/
├── .github/
│   └── workflows/
│       └── update-profile.yml
├── assets/
│   ├── hero.svg
│   ├── hero-static.svg
│   ├── hero-compact.svg
│   ├── hero-compact-static.svg
│   ├── button-portfolio.svg
│   ├── button-email.svg
│   ├── languages.svg
│   └── stack/
│       └── (১৪টা tech chip, যেমন react.svg, django.svg ...)
├── scripts/
│   ├── build-profile.mjs
│   └── icons.json
├── profile.config.json
├── README.md
└── SETUP.md
```

**সবচেয়ে সাধারণ ভুল:** বাইরের পুরো ফোল্ডারটা একসাথে টেনে আনলে ফাইলগুলো `abrarfahimabir/abrarfahimabir/README.md`-এর মতো আরেকটা ফোল্ডারের ভেতরে চলে যায়। তখন profile-এ README দেখাবে না। `README.md` যেন repository খুললেই প্রথম লিস্টে দেখা যায়।

---

## ধাপ ৫: Workflow চালু করা এবং চালানো

Workflow হলো ছোট একটা automation। এটা:

- সপ্তাহে একবার (সোমবার, বাংলাদেশ সময় সকাল ৯:১৭) GitHub থেকে আপনার public repository-গুলোর তথ্য পড়ে "GitHub activity" অংশটা আপডেট করে
- `profile.config.json` বদলালে ব্যানার আর tech chip নতুন করে বানায়
- কিছু না বদলালে কোনো commit করে না

### প্রথমবার নিজে চালিয়ে দেখুন

1. repository পেজের উপরে **Actions** ট্যাবে যান।
2. যদি একটা বার্তা দেখেন যেখানে workflow চালু করার অনুমতি চাওয়া হচ্ছে, তাহলে **I understand my workflows, go ahead and enable them** চাপুন।
3. বামদিকের লিস্ট থেকে **Update profile** বেছে নিন।
4. ডানদিকে **Run workflow** চাপুন। branch `main` রেখে সবুজ **Run workflow** বাটনটা চাপুন।
5. এক মিনিটের মতো অপেক্ষা করুন। সবুজ টিক (✓) মানে সফল।

যদি কিছু না বদলায়, তাহলে workflow কোনো নতুন commit করবে না। এটা স্বাভাবিক।

### Permission

workflow ফাইলের ভেতরেই `contents: write` permission চাওয়া আছে, তাই সাধারণত কোনো সেটিং বদলাতে হয় না। workflow শুধু আপনার নিজের repository-তে লিখতে পারে, আর কোনো token বা password দিতে হয় না।

### ৬০ দিনের নিয়ম

GitHub-এর নিয়মে public repository-তে টানা ৬০ দিন কোনো activity না থাকলে scheduled workflow নিজে থেকে বন্ধ হয়ে যায়। activity অংশে মাসের নাম ("snapshot November 2026") থাকায় workflow সাধারণত প্রতি মাসে অন্তত একবার commit করে, তাই এটা চালু থাকার কথা। তবু বন্ধ হয়ে গেলে: **Actions** → **Update profile** → **Enable workflow**।

---

## ধাপ ৬: পরে তথ্য বদলানো

GitHub-এ যেকোনো ফাইল বদলাতে: ফাইলটা খুলুন → ডানদিকে উপরে পেনসিল আইকন (**Edit this file**) → লিখুন → **Commit changes...** → **Commit changes**।

### কোন তথ্য কোথায় বদলাবেন

| যা বদলাতে চান | কোথায় |
| --- | --- |
| নাম, role, ব্যানারের নিচের লাইন | `profile.config.json` |
| Tech stack | `profile.config.json` |
| Activity থেকে কোনো repository লুকানো | `profile.config.json` → `activity.exclude` |
| Tagline, About, Featured projects, Connect, শেষ লাইন | `README.md` |
| Portfolio বা email লিংক | `README.md`-এর দুই জায়গায়: উপরের বাটন আর **Connect** অংশ |

### `profile.config.json` বদলানো

commit করার পর workflow নিজে চালু হয় এবং এক মিনিটের মধ্যে নতুন ব্যানার আর chip বানিয়ে দেয়।

JSON লেখার নিয়ম খুব কড়া। খেয়াল রাখুন:

- প্রতিটা লেখা ডাবল কোটের ভেতরে থাকবে: `"Django"`
- লিস্টের শেষ আইটেমের পরে কমা থাকবে না: `["git", "github", "vercel"]`

Tech stack-এ এই নামগুলোর লোগো আর লিংক তৈরি আছে:

```
react, javascript, html, css, tailwind, bootstrap,
python, django, drf, postgresql, sqlite, git, github, vercel
```

অন্য কোনো নাম লিখলে (যেমন `"Redux"`) chip তৈরি হবে, শুধু লোগোর জায়গায় একটা ছোট বিন্দু থাকবে। কোনো technology যোগ করার আগে নিশ্চিত হোন যে আপনার কোনো project-এ সেটা সত্যিই ব্যবহার হয়েছে।

### নতুন project যোগ করা

`README.md`-এর **Featured projects** অংশে নিচের ছাঁচটা কপি করে বসান:

```markdown
### Project-এর নাম: এক লাইনে এটা কী

কোন সমস্যার সমাধান করে, এক-দুই বাক্যে।

- **Interface:** React, ...
- **API:** Django, Django REST Framework, ...
- **Inside:** গুরুত্বপূর্ণ ২-৩টা feature, যেগুলো code-এ আসলেই আছে।

[Repository](https://github.com/abrarfahimabir/REPO-NAME) · [Live demo](https://...)
```

- live demo না থাকলে `· [Live demo](...)` অংশটা মুছে দিন।
- তিনটার বেশি project রাখবেন না। সবচেয়ে ভালো কাজগুলোই সামনে রাখুন।
- শুধু এমন লিংক দিন যেটা নিজে খুলে দেখে নিশ্চিত হয়েছেন।

### যে অংশে হাত দেবেন না

README-তে তিনটা অংশ workflow নিজে লেখে:

```
<!-- HERO:START ... -->      থেকে   <!-- HERO:END -->
<!-- STACK:START ... -->     থেকে   <!-- STACK:END -->
<!-- ACTIVITY:START ... -->  থেকে   <!-- ACTIVITY:END -->
```

এই চিহ্নগুলোর **মাঝখানে** কিছু বদলালে পরের রানে সেটা আবার আগের মতো হয়ে যাবে। চিহ্নের লাইনগুলো মুছবেন না। ভুলে মুছে ফেললে নিচের "সমস্যা সমাধান" অংশ দেখুন।

---

## ধাপ ৭: Profile-এ README দেখা যাচ্ছে কিনা নিশ্চিত হওয়া

1. খুলুন: https://github.com/abrarfahimabir
2. pinned repository-গুলোর উপরে নতুন ব্যানার আর README দেখা যাওয়ার কথা।
3. **Light আর dark দুই theme-এ দেখুন:** উপরে ডানদিকে profile ছবিতে ক্লিক → **Settings** → **Appearance** → **Theme mode** থেকে Light আর Dark পাল্টে দেখুন। ব্যানার, বাটন আর chip-এর নিজস্ব গাঢ় background আছে, তাই দুই theme-এই একরকম দেখাবে।
4. **মোবাইলে দেখুন:** ফোনের ব্রাউজারে profile খুলুন। ছোট স্ক্রিনে একটা লম্বাটে (compact) ব্যানার দেখাবে, যাতে লেখা পড়া যায়।
5. নতুন ছবি দেখাতে GitHub-এর ৫ মিনিট পর্যন্ত লাগতে পারে। তারপর পেজটা refresh করুন।

### একটা ছোট সংশোধন (profile সেটিং)

আপনার GitHub profile-এর **Website** ঘরে এখন লেখা আছে `https://www.abrarfahimx.vercel.app`। `www.` থাকায় এই ঠিকানা খোলে না। ঠিক করতে: profile পেজে **Edit profile** চাপুন → লিংকের ঘরে (Website/URL) লিখুন `https://abrarfahimx.vercel.app` → **Save**।

---

## ধাপ ৮: সমস্যা সমাধান

### ছবি দেখা যাচ্ছে না (ভাঙা ছবির আইকন)

- **ফাইল আপলোড হয়নি বা ভুল জায়গায় আছে।** `assets` ফোল্ডারে ঢুকে দেখুন ফাইলটা আছে কিনা। নাম হুবহু মিলতে হবে: `hero.svg` আর `Hero.svg` GitHub-এর কাছে আলাদা।
- **`README.md` root-এ নেই।** ধাপ ৪-এর কাঠামোর সাথে মিলিয়ে দেখুন।
- **এইমাত্র আপলোড করেছেন।** ৫ মিনিট অপেক্ষা করে refresh করুন।
- **পুরোনো ব্যানার এখনো দেখাচ্ছে।** নতুন `README.md` ঠিকমতো আপলোড হয়েছে কিনা দেখুন। repository-তে `README.md` খুলে প্রথম লাইনে `HERO:START` আছে কিনা মিলিয়ে নিন।

### Workflow fail করেছে (লাল ✗)

প্রথমে মনে রাখুন: workflow fail করলে কোনো ফাইল বদলায় না, তাই profile আগের মতোই ঠিক থাকে।

কারণ খুঁজতে: **Actions** → লাল ✗ দেওয়া রানটা → **update** job → যে ধাপে লাল চিহ্ন সেটা খুলে পড়ুন।

| Error-এ যা লেখা | মানে | সমাধান |
| --- | --- | --- |
| `profile.config.json could not be read` | JSON-এ কমা বা কোট ভুল | লাইন নম্বর দেখে কমা বা কোট ঠিক করুন |
| `README.md needs exactly one "<!-- STACK:START ... -->"` (বা HERO/ACTIVITY) | চিহ্নের লাইন মুছে গেছে বা দুবার আছে | নিচের লাইনগুলো আবার ঠিক জায়গায় বসান |
| `Could not read public data from GitHub` | GitHub সাময়িক সমস্যায় আছে, অথবা config-এ username ভুল | username ঠিক আছে কিনা দেখুন, তারপর **Re-run jobs** চাপুন |
| `Permission to ... denied to github-actions[bot]` বা `403` | workflow লেখার অনুমতি পায়নি | **Settings** → **Actions** → **General** → **Workflow permissions** → **Read and write permissions** → **Save**, তারপর আবার চালান |
| `rejected` বা `failed to push` | ঠিক একই সময়ে আপনিও কিছু commit করেছেন | শুধু **Re-run jobs** চাপুন |

মুছে যাওয়া চিহ্ন ফেরত আনতে, সঠিক section heading-এর নিচে এই জোড়াগুলো বসান (মাঝখানের অংশ workflow নিজে ভরে দেবে):

```
<!-- HERO:START (generated from profile.config.json, do not edit inside this block) -->
<!-- HERO:END -->

<!-- STACK:START (generated from profile.config.json, do not edit inside this block) -->
<!-- STACK:END -->

<!-- ACTIVITY:START (generated by the "Update profile" workflow, do not edit inside this block) -->
<!-- ACTIVITY:END -->
```

HERO জোড়াটা README-র একদম শুরুতে বসবে, STACK জোড়াটা **Tech stack**-এর নিচে, আর ACTIVITY জোড়াটা **GitHub activity**-র নিচে। তারপর **Actions** থেকে workflow একবার চালান।

---

## ঐচ্ছিক: নিজের কম্পিউটারে চালানো

কম্পিউটারে Node.js 20 বা নতুন ভার্সন থাকলে, repository ফোল্ডারে terminal খুলে চালান:

```bash
node scripts/build-profile.mjs            # সব কিছু, GitHub থেকে activity সহ
node scripts/build-profile.mjs --offline  # শুধু ব্যানার আর chip, internet ছাড়া
```

এটা ঐচ্ছিক। GitHub-এর workflow-ই একই কাজ করে দেয়।

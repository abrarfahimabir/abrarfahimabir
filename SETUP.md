# Abrar-এর GitHub Profile সেটআপ

এই ZIP-এর সব banner ও animation আগে থেকেই তৈরি। Profile দেখাতে Node.js, Python, npm, API key বা token হাতে বসাতে হবে না। Auto-update শুধু public-code snapshot ও recently pushed তালিকা আপডেট করে। Animation আপলোড করলেই চলে।

## ১. ZIP খুলুন

Windows-এ ZIP-এর ওপর Right-click → **Extract All…** → **Extract**।

Extract করা ফোল্ডারের ভেতরে ঢুকুন, যতক্ষণ না একসঙ্গে `README.md`, `assets`, `scripts` এবং `profile.config.json` দেখতে পান।

## ২. Upload পেজ খুলুন

এই লিংক খুলুন:

https://github.com/abrarfahimabir/abrarfahimabir/upload/main

Repository-এর নাম `abrarfahimabir` এবং সেটি Public থাকতে হবে।

## ৩. ফাইলগুলো টেনে দিন

File Explorer-এ ওই ফোল্ডারের ভেতরের সব ফাইল ও ফোল্ডার সিলেক্ট করুন (**Ctrl + A**)। পুরো বাইরের ফোল্ডারটি সিলেক্ট করবেন না।

সিলেক্ট করা ফাইলগুলোর ওপর মাউসের বাম বাটন চেপে ধরে রাখুন → **Alt + Tab** দিয়ে GitHub-এর Upload পেজে যান → **Drag files here…** ঘরের মধ্যে ছেড়ে দিন।

Upload তালিকায় এগুলো আছে কি না দেখুন:

- `README.md`
- `profile.config.json`
- `assets/hero.gif`
- `assets/hero-mobile.gif`
- `assets/stack-flow.gif`
- `assets/skillstream.gif`
- `assets/ostad-blog.gif`
- `assets/contact.gif`
- `scripts/build-profile.mjs`
- `data/public-code.json`

নিচে **Commit directly to the main branch** সিলেক্ট রাখুন → সবুজ **Commit changes** চাপুন। একই নামের আগের ফাইলগুলো নতুন সংস্করণ দিয়ে বদলে যাবে।

## ৪. Workflow ফাইলটি নিশ্চিত করুন

Browser upload কখনো `.github` ফোল্ডার বাদ দিতে পারে। এই লিংক খুলুন:

https://github.com/abrarfahimabir/abrarfahimabir/blob/main/.github/workflows/update-profile.yml

ফাইলটি থাকলে খুলে দেখুন `Rebuild public-code snapshot` লেখা আছে কি না। থাকলে নতুন workflow সঠিকভাবে আপলোড হয়েছে—ধাপ ৫-এ যান।

ফাইলটি না থাকলে:

1. Repository-তে **Code → Add file → Create new file** চাপুন।
2. নাম লিখুন: `.github/workflows/update-profile.yml`
3. কম্পিউটারে Extract করা ফোল্ডারের `.github` → `workflows` → `update-profile.yml` ফাইলটি **Notepad** দিয়ে খুলুন।
4. Notepad-এ **Ctrl + A → Ctrl + C** চাপুন।
5. GitHub-এর বড় code ঘরে **Ctrl + V** চাপুন।
6. **Commit changes… → Commit changes** চাপুন।

ফাইলটি থাকলেও পুরোনো content থাকলে, GitHub-এ পেনসিল আইকন দিয়ে Edit খুলে সব লেখা নতুন ZIP-এর workflow দিয়ে বদলে Commit করুন।

## ৫. Auto-update একবার চালান

1. Repository-র ওপরে **Actions** চাপুন।
2. Enable করার বার্তা থাকলে **I understand my workflows, go ahead and enable them** চাপুন।
3. বাম পাশে **Update profile** চাপুন।
4. **Run workflow ▾ → main → সবুজ Run workflow** চাপুন।
5. পেজ Refresh করুন। সবুজ ✓ হলে সফল।

নতুন ফাইল আপলোড করার পর পুরোনো failed run-এ **Re-run jobs** না দিয়ে এভাবে নতুন run শুরু করুন।

Workflow নতুন করে upload/পরিবর্তনের সময় এবং সোমবার বাংলাদেশ সময় সকাল **৯:১৭**-এ চলার জন্য সেট করা। GitHub scheduled run কিছুটা দেরিতে শুরু করতে পারে। Public repository দীর্ঘদিন নিষ্ক্রিয় থাকলে GitHub schedule বন্ধ করতে পারে; সে ক্ষেত্রে Actions-এ গিয়ে আবার Enable করুন।

## ৬. নিজের Profile দেখুন

https://github.com/abrarfahimabir

Animation ও project card দেখা যাবে। GitHub ছবি cache করলে কয়েক মিনিট পরে Refresh করুন। ফোনে বড় অক্ষরের আলাদা banner আছে। Browser reduced-motion setting সমর্থিত হলে still ছবি দেখাবে।

## সমস্যা হলে

| যা দেখা যাচ্ছে | কী করবেন |
| --- | --- |
| `Cannot find module .../scripts/build-profile.mjs` | `scripts` পুরো ফোল্ডারটি root-এ আপলোড করুন, তারপর নতুন Run workflow দিন। |
| `data/public-code.json` পাওয়া যায়নি | ZIP-এর `data` ফোল্ডারটি আপলোড করুন। |
| Update profile নেই | ধাপ ৪ অনুযায়ী workflow যোগ করুন। |
| Run workflow নেই | নতুন ZIP-এর workflow content ব্যবহার হয়েছে কি না দেখুন; ফাইলে `workflow_dispatch:` থাকতে হবে। |
| `403` বা `Permission denied` দিয়ে git push ব্যর্থ | Settings → Actions → General → Workflow permissions → Read and write permissions → Save, তারপর নতুন Run workflow দিন। Organization restriction থাকলে সেটি account owner-কে দেখতে হবে। |
| ছবি ভাঙা বা দেখা যায় না | `assets` ফোল্ডারটি root-এ আছে কি না দেখুন। README-ও root-এ থাকবে। |
| পুরোনো design ফিরে আসছে | Actions-এ অন্য পুরোনো workflow নতুন README/asset overwrite করছে কি না দেখুন। এই ZIP শুধু `update-profile.yml` ব্যবহার করে। |

পুরোনো unused banner ফাইল মুছতে হবে না। নতুন README শুধু এই ZIP-এর নতুন assets ব্যবহার করে।

## পরে কিছু বদলাতে চাইলে

- About, project description, email ও portfolio link: `README.md` Edit করুন।
- Activity থেকে repo বাদ দিতে: `profile.config.json`-এ `activity.exclude`-এ নাম যোগ করুন।
- `ACTIVITY:START` ও `ACTIVITY:END`-এর মাঝের অংশ workflow আপডেট করে। ওই দুই marker রাখুন।
- Artwork-এর লেখা বা রং বদলাতে: নিচের developer note দেখুন।

## Developer note: ঐচ্ছিক

প্রথমবার সেটআপে এই command চালাতে হবে না।

```bash
node scripts/build-profile.mjs            # GitHub-এর public data থেকে snapshot
node scripts/build-profile.mjs --offline  # ZIP-এর সংরক্ষিত snapshot থেকে; date আগেরটাই থাকবে
```

Node.js 22 বা নতুন সংস্করণ লাগবে; npm package লাগে না। GitHub Actions নিজে Node সেটআপ করে। সেখানে built-in `GITHUB_TOKEN` নিজে থেকে আসে—আপনাকে secret বানাতে হবে না।

Artwork source: `scripts/render-assets.py`; fonts ও লাইসেন্স `scripts/fonts/`-এ আছে। Optional artwork rebuild:

```bash
python -m pip install Pillow numpy
python scripts/render-assets.py
```

GitHub README JavaScript বা custom CSS web app চালায় না। এখানকার motion সব pre-rendered GIF, তাই link ছাড়া hover effect বা live UI control নেই। সব visual asset নিজের repository থেকে load হয়। Live snapshot কেবল GitHub-এর public API ব্যবহার করে; language percentage code size বোঝায়, skill level নয়।

# Brix

بريكس هو الإيجنت الأساسي لتنسيق وتنفيذ شغل UI/UX داخل Figma. تعليماته الأصلية في [AGENT.md](AGENT.md)، وتعريفه في [agents/brix.md](agents/brix.md).

أُضيفت مراجع **UI UX Pro Max** و**Impeccable** إلى مهارات بريكس من خلال [design-reference-library](skills/design-reference-library/SKILL.md). تستخدمها الأدوار الموجودة حسب الحاجة، دون استبدال طريقة الشغل أو بوابات البحث والمراجعة. المصادر والإصدارات في [sources.json](sources.json)، والتراخيص محفوظة مع المراجع.

## تثبيت بريكس في مشروع

من هذا المجلد، اختر مجلد مشروع تصميم جديد:

```sh
python3 install.py --project /absolute/path/to/design-project --dry-run
python3 install.py --project /absolute/path/to/design-project
python3 install.py --project /absolute/path/to/design-project --check
```

المثبّت ينسخ تعليمات بريكس ومهاراته كاملة إلى `.agents/skills/brix/references/bundle`، ويضيف مدخل المهارة `.agents/skills/brix/SKILL.md` وتعريف OpenCode. لا يستبدل أي ملف موجود مختلف ولا يغيّر إعدادات عامة. لإصدار جديد استخدم مجلدًا جديدًا؛ لا يوجد تحديث تلقائي.

- **Codex وCLI:** افتح المشروع واطلب `$brix`؛ المهارة متاحة في الدور التالي، أو أعد فتح الجلسة إذا لم تظهر.
- **OpenCode وCLI:** افتح المشروع واختار الإيجنت `brix`.
- **Antigravity وCLI/IDE:** افتح المشروع واطلب مهارة `brix` من مسار المهارات المشترك.

هذه مداخل لنفس بريكس، وليست إيجنتات منفصلة. تحقق التثبيت محليًا لا يثبت توافق التشغيل الفعلي داخل البرامج الثلاثة.

توثيق مسارات التثبيت: [Codex](https://learn.chatgpt.com/docs/build-skills)، [OpenCode skills](https://opencode.ai/docs/skills/)، [OpenCode agents](https://opencode.ai/docs/agents/)، [Antigravity](https://antigravity.google/docs/skills).

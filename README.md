# Linghui Meng — academic homepage

A single-file, responsive academic homepage for GitHub Pages. No dependencies or build step. White background, compact navigation, a profile sidebar, and a text-first research column are inspired by the requested reference at https://xuefuzhao.github.io/. All wording, portrait and documents are Linghui Meng's own existing materials. No reference-site content or code was copied.

## Preview and maintenance

Open `index.html` or serve this directory with `python3 -m http.server 8000`.

The separately delivered portable preview embeds the portrait and links to PDFs already hosted on the live homepage. It is not the deployment source. Source deployment uses relative PDF/image URLs.

- Edit biography, experience, publications and archives directly in `index.html`.
- Publication years mean venue publication year, or preprint release year for a preprint. Sort by that year, newest first. Papers within the same year are not date-ranked.
- Keep publication status explicit. Do not turn preprint or accepted manuscript into a conference/journal publication without verification.
- Every publication has one `data-topic`: `reasoning`, `multi-agent`, or `other`. Filtering and counts are progressive enhancement; all papers remain visible with JavaScript disabled and in print.
- Add confirmed dates to archived resources. Mark unavailable dates `Undated`; never use a file modification timestamp as a document's creation date.
- Update the footer's page-update date only when page content changes. This date does not indicate the age of linked materials.
- Replace old CV files only with a genuinely updated CV. Until then, the 2023 English CV and undated Chinese CV remain clearly archived.
- Preserve asset filenames or update matching links. There are no external fonts, frameworks, or script dependencies. Flag Counter remains a third-party resource.

## Checks

```sh
python3 tests/check_homepage.py
python3 tests/check_dates.py
node tests/check_filters.cjs
git diff --check
```

Checks cover nesting, local file references, fragment targets, duplicate IDs, metadata/accessibility hooks, date ordering and archive labels, plus filter logic and repeated selections.

## Date review — 9 October 2026

- PhD completion (2024) and ERNIE Thinking experience (2024–2025) were confirmed by Linghui Meng. CASIA is labeled as education, not a current employer.
- Added the user-confirmed Qwen Team, Alibaba research internship (2023–2024), RLHF and multi-agent learning, mentored by Junyang Lin. Added the Microsoft Research Asia speech-research internship (early–late 2020), mentored by Xu Tan, as confirmed by Linghui Meng. No exact months were inferred.
- ERNIE Thinking uses the user-requested wording: “Worked on integrating reinforcement learning (RL) updates into the ERNIE Thinking model.”
- About follows the user-confirmed chronology from 2019 graduation through the ERNIE Bot (Wenxin Yiyan) Sys2 team work on RL for subjective and objective tasks, including mathematics, coding and instruction following, until January 2026. No Sys2 start date or role after January 2026 is inferred, and the earlier ERNIE Thinking work is not assigned to Sys2 without confirmation.
- Reviewer service is described historically; specific service years are not supplied.
- The 2021–2022 news and old slides are archived. Football slides show 5 March 2021; GMM-HMM notes show 24 February–1 March 2020; the large-model talk is dated 17 March 2022. MARL and StarCraft slides have no verified date.
- The English CV is a 2023 version and still describes PhD study. The Chinese CV is undated and contains historical submission statuses. Both remain unchanged and are explicitly described as historical.
- The earlier institutional mailing address is kept in a collapsed archive disclosure, not presented as a current address. The active contact email is mengreinhold@163.com, explicitly updated by Linghui Meng on 9 October 2026. Archived PDFs retain their original contents. The historical mailing address has not been reconfirmed as current.
- M3 replaces the obsolete AAMAS 2023 acceptance placeholder. The full title and authors are supported by the official proceedings and the 2023 CV: https://aamas.csc.liv.ac.uk/Proceedings/aamas2023/pdfs/p1624.pdf .
- MADT now uses its 2023 journal version, title, author list and pagination (Machine Intelligence Research 20(2), 233–248), with its 2021 preprint retained as a secondary link: https://link.springer.com/article/10.1007/s11633-022-1383-7 .
- The NSR survey remains correctly labeled an accepted manuscript in 2026. The publisher gives 24 September 2026: https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag599/8834022 .
- ERNIE 5.0 is a 2026 technical report: https://arxiv.org/abs/2602.04705 . A2R remains a 2025 preprint: https://arxiv.org/abs/2509.22044 .
- Five 2024 papers retain their verified conference years. ViLaS's 2023 preprint date is distinct from its ICASSP 2024 publication: https://arxiv.org/abs/2305.19972 .
- ICAPS 2022 metadata uses https://ojs.aaai.org/index.php/ICAPS/article/view/19850 . Other earlier venue years remain unchanged.
- The publication list is not claimed to be exhaustive. No current employer, unknown date, or new employment claim was inferred.

## Verification limits

The reference and currently deployed homepage were inspected visually in the cloud browser. The revised source passed static and filter-logic checks, but desktop/mobile browser rendering of the revised local file remains unverified: the cloud browser permits only HTTP(S) pages and rejected the local data-URL preview. Prior local Chromium startup was unavailable in this environment. No screenshot of this revision is represented as browser-verified. These checks do not verify deployment.

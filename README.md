# Linghui Meng — academic homepage

A responsive, self-contained HTML homepage for GitHub Pages. No package installation or build step is required. The existing `_config.yml` and all PDF/image assets are retained.

## Preview

Open `index.html` in a browser, or run `python3 -m http.server 8000` in this directory and visit `http://localhost:8000`. The delivery also includes a separate portable preview with an embedded portrait and absolute links to the existing PDFs; that preview is not the deployment source.

## Maintain

- Edit biography and publications directly in `index.html`.
- Each publication uses `data-topic="reasoning"`, `"multi-agent"`, or `"other"` for the accessible filters. All papers remain visible when JavaScript is disabled.
- Update the two `counter-reset: paper` values to one more than the number of entries when adding or removing a paper. The live filter count is calculated automatically.
- Keep asset filenames unchanged or update their matching links. URLs with spaces are percent-encoded.
- CSS is inline so the homepage remains easy to edit as a single file. There are no external fonts, frameworks, or script dependencies.
- The original Flag Counter is retained and remains a third-party resource.

## Checks

```sh
python3 tests/check_homepage.py
node tests/check_filters.cjs
git diff --check
```

These check HTML nesting, local file references, fragment targets, duplicate IDs, headings, metadata and accessibility hooks, plus filter behavior, repeated selections and the live count. They do not replace browser/assistive-technology testing.

## Review notes — 9 October 2026

- PhD completion in 2024 was confirmed by Linghui Meng. No current employer is inferred.
- Added the user-confirmed 2024–2025 ERNIE Thinking experience: “Led the integration of reinforcement learning (RL) updates into the ERNIE Thinking model.” No employer or further responsibilities are inferred.
- The Google Scholar profile is verified: https://scholar.google.com/citations?user=YF0Hy1sAAAAJ&hl=en . Eight 2024–2026 works have been added using this identity and publisher/arXiv metadata.
- The ICAPS 2022 paper title and link were corrected using the official proceedings: https://ojs.aaai.org/index.php/ICAPS/article/view/19850 .
- The MADT title follows the latest version at https://arxiv.org/abs/2112.02845 .
- The original AAMAS 2023 placeholder title/authors remain pending confirmation. Its incorrect link to the GCS 2022 paper has been removed. M3 is a likely match, but that mapping has not been confirmed.
- Both original CV files remain unchanged. The English filename dates from 2023 and may need a new version.
- The contact email and postal address are retained from the original page; their current status was not reconfirmed. The phrase “route packaging” is a spelling correction of the original “route packeging”; its intended technical wording may need review.
- These changes are proposed for review in a draft pull request. Merging, deployment, and hosting migration are outside this update.
- Static checks and filter logic tests passed. Visual/browser QA could not run in this environment: Chromium startup cannot create a required Unix socket, and the available cloud browser cannot access the local preview server. Desktop/mobile screenshots and rendered accessibility/contrast checks therefore remain unverified.

## New publication sources

- A Survey on Parallel Reasoning: https://doi.org/10.1093/nsr/nwag599 (National Science Review, accepted manuscript, 2026)
- ERNIE 5.0 Technical Report: https://arxiv.org/abs/2602.04705 (2026)
- A2R: https://arxiv.org/abs/2509.22044 (2025)
- A New Pre-Training Paradigm for Offline Multi-Agent Reinforcement Learning with Suboptimal Data: https://doi.org/10.1109/ICASSP48485.2024.10448500
- UNeC: https://doi.org/10.1109/ICASSP48485.2024.10447360
- ViLaS: https://arxiv.org/abs/2305.19972 and https://doi.org/10.1109/ICASSP48485.2024.10448450
- Long Short-Term Reasoning Network with Theory of Mind for Efficient Multi-Agent Cooperation: https://doi.org/10.1109/IJCNN60899.2024.10650244
- SA-MPF: https://doi.org/10.1109/IJCNN60899.2024.10650103

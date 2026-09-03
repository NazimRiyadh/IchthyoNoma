# IchthyoNoma

**Nomenclature and Context Sensitivity of Zero-Shot Biological Vision-Language Models for Bangladeshi Freshwater Fish Recognition**

This repository accompanies an anonymous MusIML @ NeurIPS 2026 submission on the stability of zero-shot biological vision-language model (VLM) evaluation under changes in biological specialization, language, nomenclature, prompt formulation, and visual context.

## Highlights

- **10,321 source images** from two public Bangladeshi freshwater-fish sources: BFF-15 (2,656) and SylFishBD (7,665).
- **Seven shared classes:** Rui, Katla, Mrigal, Tilapia, Pabda, Ilish, and Koi.
- **Frozen zero-shot models:** CLIP ViT-B/32, BioCLIP, BioCLIP2, plus Jina CLIP v2 as a multilingual diagnostic control.
- **Text-side stress tests:** Romanized vernacular, Bengali script, English-common names, scientific names, prompt templates, and scientific synonyms.
- **Paired context interventions:** graded background blur, neutral/white masking, crop, background-only views, and cross-species background swaps.
- **Paired inference:** class-stratified bootstrap confidence intervals, exact McNemar tests, Benjamini-Hochberg FDR correction, Cochran's Q, and permutation tests.

Selected findings from the current paper snapshot:

- BioCLIP2 reaches **72.36%** BFF-15 accuracy with English-common names and **68.91%** SylFishBD accuracy with scientific names.
- BioCLIP2 Bengali-script prompts are near chance in balanced accuracy (**14.22-14.29%**).
- Jina CLIP v2 partially recovers Bengali balanced accuracy to **21.89%** on BFF-15 and **16.36%** on SylFishBD, but bare Bengali names return to **14.29%** on both sources.
- Strong background blur changes overall SylFishBD accuracy by **-2.87 pp**, while a white mask produces a larger **-8.39 pp** drop.
- Context effects are strongly class-dependent: under strong blur, Katla and Mrigal improve while Rui declines sharply.

## Repository structure

```text
IchthyoNoma/
├── README.md
├── requirements.txt
├── requirements-kaggle.txt
├── .gitignore
├── CITATION.cff.template
├── data/
│   └── README.md
├── docs/
│   ├── REPRODUCIBILITY.md
│   ├── NOTEBOOK_PROVENANCE.md
│   └── RELEASE_CHECKLIST.md
├── notebooks/
│   ├── README.md
│   ├── 01_primary_zero_shot_benchmark.ipynb
│   ├── 02_context_robustness_controls.ipynb
│   └── 03_multilingual_jina_control.ipynb
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── anonymous_submission.pdf
│   ├── overview_updated.png
│   └── context_selected_effects.pdf
├── results/
│   ├── README.md
│   ├── primary_zero_shot_benchmark.csv
│   ├── context_ladder.csv
│   ├── jina_multilingual_metrics.csv
│   └── jina_pairwise_language_tests.csv
└── scripts/
    ├── validate_dataset_counts.py
    └── verify_release_results.py
```

## Reproduction status

The repository includes the **paper source**, **paper-level result tables**, and three executable analysis notebooks. The Jina notebook is retained from the working experiment. The primary-benchmark and context-control notebooks are clearly marked **reference/reproducibility implementations reconstructed from the documented paper protocol**, not exact historical execution files. See [`docs/NOTEBOOK_PROVENANCE.md`](docs/NOTEBOOK_PROVENANCE.md).

For a definitive archival code release, replace the two reference notebooks with the exact original executed notebooks if available, after removing credentials and machine-specific paths. Do not claim the reference implementations are the historical files.

## Data

The datasets are **not redistributed** in this repository. See [`data/README.md`](data/README.md) for expected classes, counts, and setup notes.

## Environment

For a general local environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

For the Jina multilingual experiment on Kaggle, prefer the lighter dependency file:

```bash
pip install -r requirements-kaggle.txt
```

The Kaggle notebook intentionally avoids upgrading Kaggle's NumPy/Pandas/SciPy stack.

## Paper

The anonymous submission snapshot is in [`paper/anonymous_submission.pdf`](paper/anonymous_submission.pdf). The LaTeX source expects the official `neurips_2026.sty` file to be supplied by the conference/workshop template; that style file is not redistributed here.

## Verification

Check the aggregate release tables with:

```bash
python scripts/verify_release_results.py
```

Check a local dataset layout/counts with:

```bash
python scripts/validate_dataset_counts.py /path/to/dataset --target BFF-15
python scripts/validate_dataset_counts.py /path/to/dataset --target SylFishBD
```

## Anonymity note for double-blind review

If the workshop review is double blind, **do not publish this repository from a personally identifying GitHub account before the anonymity period ends unless the venue explicitly permits it**. A private repository is safer during review. If code must be supplied to reviewers, use an anonymized supplementary archive/link consistent with the venue's rules.

## Citation

A citation template is provided as `CITATION.cff.template`. Fill in the final author list, release date, repository URL, and arXiv/DOI information only after they are public.

## License

No software license is asserted by this release candidate. Before making the repository public, choose a code license that all authors approve and verify the redistribution terms of any included third-party assets. The datasets themselves remain subject to their original licenses/terms.

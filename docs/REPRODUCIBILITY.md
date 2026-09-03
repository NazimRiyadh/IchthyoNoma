# Reproducibility guide

## 1. Obtain data

Follow `data/README.md`. The expected harmonized totals are 2,656 BFF-15 images and 7,665 SylFishBD source images.

## 2. Environment

Create a clean Python environment and install `requirements.txt`. For Kaggle/Jina only, use `requirements-kaggle.txt` to avoid upgrading Kaggle's core scientific stack.

## 3. Primary zero-shot protocol

The paper's primary model family is:

- CLIP ViT-B/32 with OpenAI weights
- BioCLIP (`imageomics/bioclip`)
- BioCLIP2 (`imageomics/bioclip-2`)

For each class name, four text templates are embedded:

1. `a photo of {name}, a fish species`
2. `an image of {name}, a fish species`
3. `a photograph of {name}, a fish species`
4. `a specimen of {name}, a fish species`

Each template embedding is L2-normalized; class prototypes are formed by averaging the normalized embeddings and L2-normalizing the mean. Image embeddings are cached per model/condition.

## 4. Nomenclature controls

Prompt families:

- Romanized vernacular
- Bengali script
- English common
- scientific binomial

Scientific synonym controls include Katla and Mrigal variants described in the paper.

## 5. Multilingual diagnostic

Run `notebooks/03_multilingual_jina_control.ipynb` after verifying Bengali label strings and dataset counts. The paper-matched four-template result is primary; bare class names are a secondary control.

## 6. Context interventions

SylFishBD masks support paired interventions:

- weak/medium/strong Gaussian background blur
- gray, mean-color, and white masks
- tight crop
- background-only inpainting
- cross-species background swap

The original robustness notebook should be included before public release so these image transformations can be reproduced exactly.

## 7. Statistics

- Primary cross-model benchmark: 1,000 class-stratified bootstrap resamples
- Robustness and multilingual controls: 2,000 class-stratified bootstrap resamples
- exact two-sided McNemar tests for paired correctness
- Benjamini-Hochberg FDR correction within analysis families
- Cochran's Q for context conditions
- 5,000 label permutations for background-swap donor-follow analysis
- random seed: 42

## 8. Sanity checks

Run:

```bash
python scripts/verify_release_results.py
```

This checks that the aggregate CSVs in `results/` match the values reported in the release snapshot.


## Notebook execution order

1. `notebooks/01_primary_zero_shot_benchmark.ipynb`
2. `notebooks/02_context_robustness_controls.ipynb`
3. `notebooks/03_multilingual_jina_control.ipynb`

See `docs/NOTEBOOK_PROVENANCE.md` before describing the first two files as original execution artifacts.

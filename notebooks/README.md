# Notebooks

The repository now contains three experiment notebooks:

1. **`01_primary_zero_shot_benchmark.ipynb`** — CLIP/BioCLIP/BioCLIP2 benchmark, prompt families, Bengali BioCLIP2 control, template sensitivity, and scientific-name variants.
2. **`02_context_robustness_controls.ipynb`** — paired SylFishBD blur/mask/crop/background-only/background-swap controls and paired statistical helpers.
3. **`03_multilingual_jina_control.ipynb`** — Jina CLIP v2 multilingual diagnostic control.

## Provenance

`03_multilingual_jina_control.ipynb` is the working Jina notebook retained from this project. The current `01_...` and `02_...` files are **clean reference/reproducibility implementations reconstructed from the protocol documented in the paper**; they are not claimed to be byte-for-byte copies of the original executed ICCIT/Kaggle notebooks. If the exact historical notebooks are available, replace these two reference files before a definitive archival release, after removing credentials and machine-specific paths.

The notebooks intentionally keep dataset roots configurable and do not redistribute BFF-15 or SylFishBD images.

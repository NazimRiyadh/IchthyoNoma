# Data setup

This repository does **not** redistribute the source images or masks.

## Seven harmonized classes

| Class | BFF-15 | SylFishBD |
|---|---:|---:|
| Rui | 514 | 1,670 |
| Katla | 427 | 1,133 |
| Mrigal | 317 | 1,293 |
| Tilapia | 383 | 1,326 |
| Pabda | 348 | 862 |
| Ilish | 233 | 789 |
| Koi | 434 | 592 |
| **Total** | **2,656** | **7,665** |

All selected SylFishBD source images have a paired segmentation mask in the study protocol.

## BFF-15

Paper reference: **Bangladeshi Freshwater Fish Image Dataset (BFF-15)**.

Kaggle source used in the paper:

`https://www.kaggle.com/datasets/theshahidul/bangladeshi-freshwater-fish-image-dataset-bff-15`

The public source may contain additional folders/classes. The study uses only the seven classes above.

## SylFishBD

Use the public SylFishBD source corresponding to the paper citation:

S. Absar et al., *A freshwater fish dataset for visual recognition with manually localized ROIs and SAM-derived instance masks*, Scientific Data, 2026.

The study selects the same seven overlapping classes and expects 7,665 raw/mask pairs.

## Folder-name robustness

The released Jina notebook includes aliases for common Tilapia folder spellings (`Tilapia`, `Telapia`, `Telapiya`, `Tilapiya`) because public mirrors can differ in folder naming.

Before inference, validate counts with:

```bash
python scripts/validate_dataset_counts.py /path/to/root --target BFF-15
python scripts/validate_dataset_counts.py /path/to/root --target SylFishBD
```

Do not silently continue when counts differ from the paper snapshot.

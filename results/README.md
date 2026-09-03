# Aggregate results

These CSVs provide machine-readable versions of central aggregate results from the current paper/release snapshot.

They are intended for verification and plotting. They do **not** replace per-image predictions or the original execution notebooks.

- `primary_zero_shot_benchmark.csv`: CLIP/BioCLIP/BioCLIP2 accuracy and macro-F1.
- `context_ladder.csv`: BioCLIP2 paired SylFishBD context ladder under scientific prompts.
- `jina_multilingual_metrics.csv`: Jina CLIP v2 primary four-template and name-only metrics.
- `jina_pairwise_language_tests.csv`: paired accuracy differences, bootstrap CIs, exact McNemar p-values, and FDR q-values for the primary Jina language comparisons.

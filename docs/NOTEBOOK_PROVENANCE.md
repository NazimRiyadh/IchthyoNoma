# Notebook provenance

This release distinguishes between **working execution notebooks** and **reference reimplementations**.

- `notebooks/03_multilingual_jina_control.ipynb`: working notebook from the multilingual-control experiment.
- `notebooks/01_primary_zero_shot_benchmark.ipynb`: clean reference implementation reconstructed from the paper's stated model/checkpoint, prompt, class, and metric protocol.
- `notebooks/02_context_robustness_controls.ipynb`: clean reference implementation reconstructed from the paper's stated paired intervention and statistical protocol.

The two reference notebooks are supplied so the GitHub repository has executable, auditable code for every analysis family. They must not be described as the exact historical execution files unless they are later replaced by those originals. Aggregate CSVs in `results/` preserve the reported paper values.

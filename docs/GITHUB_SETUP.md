# GitHub setup

Suggested repository name:

`IchthyoNoma`

Suggested one-line description:

> Auditing nomenclature, multilingual alignment, prompt formulation, and visual context in zero-shot biological VLMs for Bangladeshi freshwater fish recognition.

Suggested topics after de-anonymization/public release:

`vision-language-models`, `bioclip`, `clip`, `zero-shot-learning`, `biodiversity`, `fish-classification`, `multilingual`, `bengali`, `robustness`, `computer-vision`

## During double-blind review

Prefer a **private** repository unless the venue explicitly permits a public, identifying code repository. Do not place author names, personal email addresses, ORCID IDs, institution names, profile badges, or personal GitHub links in the anonymous review snapshot.

## Local Git commands

From the repository directory:

```bash
git init
git branch -M main
git add .
git commit -m "Initial anonymous research release"
```

After creating the remote repository on GitHub:

```bash
git remote add origin https://github.com/OWNER/IchthyoNoma.git
git push -u origin main
```

For a private review-period repository, create the remote as **Private**. After the anonymity period, update `CITATION.cff.template`, add the chosen license, add author information, and optionally make the repository public.

## Recommended release tags

- `v0.1-musiml-submission` — anonymous submission snapshot
- `v0.2-camera-ready` — author-visible camera-ready snapshot
- `v1.0` — archival/public reproducibility release

# Public release checklist

Before making the GitHub repository public:

- [ ] Confirm the venue permits public code during double-blind review; otherwise keep the repo private/anonymized.
- [ ] Add the exact primary benchmark notebook used for reported results.
- [ ] Add the exact context-robustness notebook used for reported results.
- [ ] Remove API tokens, Kaggle credentials, private file paths, usernames, and local machine metadata.
- [ ] Strip large notebook outputs and cached embeddings unless intentionally released.
- [ ] Verify the seven Bengali label strings with the author team.
- [ ] Re-run `python scripts/verify_release_results.py`.
- [ ] Add author names to `CITATION.cff` only when anonymity is no longer required.
- [ ] Choose and add a code license approved by all authors.
- [ ] Confirm dataset terms permit any screenshots/sample images included in the repository.
- [ ] Add final arXiv/DOI/OpenReview links once public.
- [ ] Tag the paper-submission snapshot (for example `v0.1-musiml-submission`).

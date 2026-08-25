# Documentation

Technical documentation for the **BovDB** dataset and `bovdb` Python SDK.

---

## Contents

| Document | Description |
|---|---|
| [`architecture.md`](architecture.md) | Relational ER model, table relationships, and database design decisions |
| [`data-dictionary.md`](data-dictionary.md) | Complete schema reference — columns, types, constraints, and descriptions for all tables (`company`, `ticker`, `price`, `price5`) |
| [`provenance.md`](provenance.md) | End-to-end data lineage — source feeds (B3 COTAHIST, CVM), extraction, harmonization pipeline, and quality gates |
| [`reproducibility.md`](reproducibility.md) | Standards for reproducible ML benchmarks — random seeds, train/test splitting, and deterministic evaluation |
| [`governance.md`](governance.md) | Repository governance — branch protection rules, PR review policy, semantic commit conventions, and release flow |

---

## Quick Links

- **Schema**: How are tables related? → [`architecture.md`](architecture.md)
- **Columns**: What does each field mean? → [`data-dictionary.md`](data-dictionary.md)
- **Where does the data come from?** → [`provenance.md`](provenance.md)
- **How to reproduce experiments?** → [`reproducibility.md`](reproducibility.md)
- **How to contribute?** → [`governance.md`](governance.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md)

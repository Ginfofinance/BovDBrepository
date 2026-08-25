# Contributing to BovDB

Thank you for your interest in contributing to **BovDB** (A dataset of stock quotes for Machine Learning on all companies from B3). Contributions to code, documentation, data verification scripts, and methodological robustness are warmly welcomed.

---

## 1. How to Contribute

1. **Issues**: Open an issue before submitting significant changes so that the research scope, bug, or feature proposal can be aligned.
2. **Branches**: Create a feature branch with a descriptive name (e.g., `feature/data-loader-optimization` or `fix/price5-datetime-parsing`).
3. **Focused Pull Requests**: Keep PRs focused on a single topic. Avoid bundling refactors, new scripts, and large benchmark artifacts into a single PR.
4. **Data and Privacy**: Never commit credentials, private keys, raw database dump files (`.db`, `.rar`, `.zip`), or proprietary market feeds to the repository.

---

## 2. Development & Testing Workflow

### Environment Setup
```bash
git clone https://github.com/Ginfofinance/BovDBrepository.git
cd BovDBrepository
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### Local Verification
Ensure all Python files compile cleanly and pass syntax checks:
```bash
python -m compileall -q src Codes
```

---

## 3. Scientific and Research Standards

When contributing scripts, algorithms, or analysis notebooks:
- **Reproducibility**: Explicitly record random seeds, software versions, and query parameters.
- **Factor adjustments**: Clearly document whether price columns are adjusted using `factor` (stock splits/dividends).
- **Documentation**: Provide clear docstrings for all functions and explanatory markdown cells in notebooks.
- **Academic Citation**: Ensure any derivative work cites the official BovDB paper (see [reference.md](reference.md) or [CITATION.cff](CITATION.cff)).

---

## 4. Pull Request Guidelines

Before submitting your PR:
- [ ] Run syntax checks via `python -m compileall -q src Codes`.
- [ ] Verify that paths to the SQLite database use flexible parameters or the `bovdb` module.
- [ ] Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
- [ ] Complete the [Pull Request Template](.github/pull_request_template.md).

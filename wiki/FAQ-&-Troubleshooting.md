# ❓ FAQ & Troubleshooting

### Q: Where should I place the SQLite database file?
**A:** Place the extracted `DataBase.db` (or `Database_define.db`) in the `DataBase/` directory at the root of the cloned repository, or set the `BOVDB_PATH` environment variable.

### Q: Does the database contain dividends and interest on equity (JCP)?
**A:** BovDB provides nominal transaction prices and corporate action adjustment factors (`factor`) for splits and inplits. Cash dividends are documented in the corporate event tables of future Medallion releases.

### Q: How do I install the package directly from GitHub Packages?
**A:** Run:
```bash
pip install --index-url https://token:<YOUR_GITHUB_TOKEN>@pypi.pkg.github.com/Ginfofinance/ simple bovdb
```
Or install in editable mode from the repository root:
```bash
pip install -e .
```

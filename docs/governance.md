# Repository Governance & Branch Protection Specification

## 1. Branch Protection Policy for `main`

To maintain scientific integrity and prevent untested or accidental modifications to canonical data and code, the `main` branch must have strict branch protection rules enforced in GitHub:

```text
Repository Settings -> Branches -> Add branch protection rule: main
```

### Required Configuration Rules:
1. **Require a pull request before merging**:
   - Require at least **1 approving review** from a core maintainer.
   - Dismiss stale pull request approvals when new commits are pushed.
2. **Require status checks to pass before merging**:
   - Require `Compile & Validate Python Scripts` (CI matrix across Python 3.10, 3.11, 3.12).
   - Require `Run Functional Test Suite (pytest)` to pass with 0 failures.
3. **Require branches to be up to date before merging**:
   - Guarantees test execution against the latest target head.
4. **Block Force Pushes**:
   - Disable `--force` pushes to protect commit provenance.
5. **Block Branch Deletion**:
   - Prevent accidental deletion of the `main` branch.

---

## 2. Commit & Pull Request Discipline

Contributors and maintainers must follow Conventional Commits:
- `feat(...)`: New features, query helpers, or API additions.
- `fix(...)`: Bug fixes, connection handling, or correction of calculations.
- `docs(...)`: Documentation, data dictionary updates, or provenance details.
- `test(...)`: Unit, integration, or functional test suite updates.
- `ci(...)`: GitHub Actions, automated package publishing, or CI scripts.
- `chore(...)`: Maintenance, dependency version bumps, or housekeeping.

Pull requests should remain **focused and atomic** to facilitate peer review and scientific auditability.

---

## 3. Versioning Strategy

* **Python SDK (`bovdb`)**: Follows Semantic Versioning (`MAJOR.MINOR.PATCH`, starting at `0.1.0`).
* **Dataset Versions**: Identifies dataset publication releases (`v1.0`, `v2.0`, `v3.0`).
* **Release Pipeline**: Releases are tagged with Git tags (`v*.*.*`), triggering automated build, checksum validation, and GitHub Package publication via GitHub Actions.

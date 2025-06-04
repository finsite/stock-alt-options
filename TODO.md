# 📌 Project TODO: Template Python Repository

This TODO list outlines enhancements and checks to ensure all repositories
derived from `template_python` are production-grade, maintainable, and
GitOps-ready.

---

## ✅ Core Functionality

- [ ] Define clear application entrypoint (`main.py`, CLI, or server)
- [ ] Support modular `src/` structure (`src/app/` or renamed)
- [ ] Include sample usage patterns (scripts, classes, handlers)
- [ ] Include default error handling and logging setup

---

## 🔐 Secure Configuration Support

- [ ] Support environment variable loading via `config.py`
- [ ] Support secure secret loading via:
  - [ ] HashiCorp Vault (optional)
  - [ ] AWS SSM Parameter Store (optional)
- [ ] Include fallback with safe warnings
- [ ] Log missing config keys clearly

---

## 📦 Dependency & Runtime Management

- [ ] Define base dependencies in `requirements.in`
- [ ] Define dev/test dependencies in `requirements-dev.in`
- [ ] Lock via `pip-compile`
- [ ] Add `Makefile` targets for:
  - [ ] `install`, `test`, `lint`, `format`, `build`, `docker-build`

---

## 🧪 Testing & Validation

- [ ] Set up `pytest` with basic coverage
- [ ] Add `tests/unit/` and `tests/integration/` directories
- [ ] Include mocks for:
  - [ ] External APIs
  - [ ] Secret stores
  - [ ] File and network I/O
- [ ] Enforce >90% coverage for new projects

---

## ⚙️ Tooling & Automation

- [ ] Include `pre-commit` with:
  - [ ] `ruff`, `black`, `mypy`, `yamlfix`, `check-pyproject`
- [ ] Configure GitHub Actions workflows:
  - [ ] Lint
  - [ ] Test + coverage
  - [ ] Pre-commit check
- [ ] Optional versioning with:
  - [ ] `Commitizen`
  - [ ] GitHub release automation

---

## 📝 Documentation

- [ ] Add project `README.md` with:
  - [ ] Overview, setup, usage
  - [ ] Developer workflow
- [ ] Add `CONTRIBUTING.md` for contributor guidance
- [ ] Add `TODO.md` with project goals
- [ ] Ensure license file (Apache 2.0)
- [ ] Include documentation generator (e.g., MkDocs or Docusaurus)

---

## 🔊 Logging

- [ ] Configure environment-based `LOG_LEVEL`
- [ ] Use structured logging (`loguru`, `structlog`, or `logging`)
- [ ] Include timestamps, context, and correlation ID support

---

## 📈 Metrics & Monitoring (Optional)

- [ ] Add Prometheus-style metrics hooks
  - [ ] `track_runtime_metrics()`
  - [ ] `track_api_latency()`
- [ ] Include stub for health check or readiness probe

---

## 🐳 Dockerization

- [ ] Provide `Dockerfile` (multi-stage if needed)
- [ ] Include `.dockerignore`
- [ ] Buildable with `make docker-build`

---

## ☸️ Kubernetes Scaffolding (Optional)

- [ ] Include `k8s/` directory with:
  - [ ] Deployment or Job YAML
  - [ ] ConfigMap and Secret stubs
  - [ ] Optional Helm chart starter

---

## 🔐 Security & Compliance (Optional)

- [ ] Generate SBOM (via `syft` or `cyclonedx`)
- [ ] Sign container image (via `cosign`)
- [ ] Ensure REUSE license compliance

---

## 🧹 Code Hygiene & Quality

- [ ] Enforce:
  - [ ] Type annotations (with `mypy`)
  - [ ] Docstrings
  - [ ] Minimal cyclomatic complexity
- [ ] Remove dead code and unused imports

---

## 🧭 Repository Template Maintenance

- [ ] Ensure all derived repos:
  - [ ] Replace `template_python` references
  - [ ] Update metadata in `pyproject.toml`
  - [ ] Customize README and LICENSE
- [ ] Optionally include `init.sh` or checklist script for first-time setup

Here's the updated section for your `TODO.md` in `template_python` (or
equivalent), under a new **Security & Compliance Workflows** heading:

---

### 🛡️ Security & Compliance Workflows

- [ ] Templatize `security.yml` GitHub Action:

  - [ ] Include `bandit` by default
  - [ ] Optional: comment-in support for `safety`, `syft`, `semgrep`, `cosign`
  - [ ] Ensure it uses stable Python version (e.g. `3.11`)
  - [ ] Target `src/` or appropriate directory

- [ ] Create `scripts/copy-security-workflow.sh` to assist with rollout
- [ ] Document checklist for verifying workflow before applying to other repos
- [ ] Add SBOM and signature tooling (e.g., `syft`, `cosign`) to future-ready
      projects
- [ ] Include pre-commit or CI check to ensure the security workflow is present
      in derived repositories

---

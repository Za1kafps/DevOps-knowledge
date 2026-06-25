# Supply Chain Security

`Supply Chain Security` — защита пути от source code до production artifact.

Цепочка:

```text
developer
  -> Git
  -> CI
  -> dependencies
  -> build
  -> image
  -> registry
  -> deploy
  -> runtime
```

---

# Что защищать

```text
Git access
branch protection
CI runner trust
dependencies
build scripts
container base images
registry permissions
artifact signatures
SBOM
deployment credentials
```

---

# Практики

```text
protected branches/tags
required reviews
dependency pinning/lockfiles
SAST/dependency/container scans
SBOM generation
image signing
OIDC short-lived deploy credentials
least privilege CI tokens
provenance/attestations
```

---

# Container image

Проверять:

```text
base image pinned
no latest
no secrets in layers
scan CVE
non-root user
minimal runtime
digest for deploy
```

Смотри [[Image Security]].

---

# Частые ошибки

## CI runner выполняет untrusted code с prod secrets

Fork/MR pipeline не должен получать production secrets.

## Dependencies без lockfile

Build не воспроизводится.

## Deploy по mutable tag

`latest` может указывать на что угодно.

---

# Связанные заметки

- [[CI-CD]]
- [[Image Security]]
- [[Secrets in CI-CD]]
- [[OIDC in CI-CD]]
- [[Container Registry]]

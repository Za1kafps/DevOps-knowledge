# Image Security

`Image Security` — безопасность container image до запуска.

Это про то, что попало в image:

```text
base image
packages
dependencies
secrets
build artifacts
SBOM
vulnerabilities
signature
provenance
```

Отдельно смотри [[Container Security]] — там про runtime.

---

# Base image

Base image задаёт основу безопасности.

Плохо:

```dockerfile
FROM ubuntu:latest
```

Лучше:

```dockerfile
FROM debian:12-slim
FROM alpine:3.20
FROM gcr.io/distroless/static-debian12
```

Выбор зависит от приложения. Alpine маленький, но musl может ломать некоторые бинарники. Distroless безопаснее по attack surface, но сложнее debug.

---

# Не использовать latest

`latest` — изменяемый tag.

Сегодня и завтра он может указывать на разные images.

Лучше:

```dockerfile
FROM nginx:1.27-alpine
```

Для максимальной воспроизводимости:

```dockerfile
FROM nginx@sha256:...
```

---

# Secrets не должны попадать в image

Проверять:

```bash
docker history --no-trunc image
docker save image -o image.tar
```

Опасно:

```dockerfile
COPY .env .
ARG TOKEN
RUN echo "$TOKEN"
```

Для build-time secret используй [[BuildKit]] secret mounts.

---

# Vulnerability scanning

Сканеры ищут CVE в OS packages и dependencies.

Примеры инструментов:

```text
Trivy
Grype
Docker Scout
GitLab container scanning
GitHub code scanning integrations
```

Пример:

```bash
trivy image registry.example.com/app:1.0.0
```

Важно: CVE scanner помогает найти известные проблемы, но не доказывает, что image безопасен полностью.

---

# SBOM

SBOM — Software Bill of Materials.

Это список компонентов image:

```text
packages
libraries
versions
licenses
```

SBOM полезен при incident response: когда выходит CVE, можно быстро понять, какие images затронуты.

---

# Signing

Image signing подтверждает, что image выпущен доверенным pipeline.

Идея:

```text
CI build -> sign image -> deploy проверяет signature
```

Инструменты:

```text
cosign
notation
registry policy
admission controller
```

---

# Практический checklist

- base image pinned по версии
- нет `latest` в production
- используется multi-stage
- нет secrets в layers
- non-root user
- image scan в CI
- SBOM сохраняется
- production deploy использует tag + digest
- registry имеет retention policy

---

# Связанные заметки

- [[Docker Image]]
- [[Dockerfile]]
- [[Multi-stage Build]]
- [[BuildKit]]
- [[Container Registry]]
- [[Supply Chain Security]]

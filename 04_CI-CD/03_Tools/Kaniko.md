# Kaniko

`Kaniko` — инструмент для сборки container images без Docker daemon.

Его часто использовали в Kubernetes CI, где нельзя или не хочется запускать privileged Docker-in-Docker.

---

# Как работает

Kaniko читает Dockerfile, build context и собирает image userspace-способом, после чего push-ит image в registry.

Пример:

```bash
/kaniko/executor \
  --context "$CI_PROJECT_DIR" \
  --dockerfile "$CI_PROJECT_DIR/Dockerfile" \
  --destination "registry.example.com/app:$CI_COMMIT_SHA"
```

---

# Плюсы

```text
не нужен Docker daemon
удобно в Kubernetes executor
можно push сразу в registry
```

---

# Минусы

```text
cache отличается от Docker/BuildKit
не все Dockerfile edge cases одинаковы
проектный статус и актуальность надо проверять перед выбором
```

Во многих новых проектах стоит рассмотреть BuildKit/buildx или Buildah.

---

# Частые проблемы

## Не может push в registry

Проверь registry credentials.

## Cache не работает как ожидалось

Kaniko cache надо настраивать отдельно.

## Dockerfile использует unsupported поведение

Проверяй совместимость и logs executor.

---

# Связанные заметки

- [[Docker in Docker]]
- [[Buildah]]
- [[BuildKit]]
- [[Container Registry]]
- [[GitLab Runner]]

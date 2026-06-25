# GitLab Container Registry

`GitLab Container Registry` — registry для container images внутри GitLab project/group.

Обычно используется вместе с [[GitLab CI]].

---

# Важные переменные CI

```text
CI_REGISTRY
CI_REGISTRY_IMAGE
CI_REGISTRY_USER
CI_REGISTRY_PASSWORD
CI_COMMIT_SHA
```

---

# Пример push

```bash
docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" .
docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
```

---

# Tags

Хорошо:

```text
$CI_COMMIT_SHA
v1.2.3
main-$CI_COMMIT_SHORT_SHA
```

Плохо для production:

```text
latest
```

---

# Частые проблемы

## denied: access forbidden

Job token или deploy token не имеет прав.

## image not found

Неверный path или tag.

## registry storage разросся

Настраивай cleanup policies.

---

# Связанные заметки

- [[GitLab CI]]
- [[Container Registry]]
- [[Docker Image]]
- [[CI-CD]]

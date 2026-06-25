# Container Registry

`Container Registry` — хранилище container images.

CI собирает image и отправляет его в registry, а runtime потом скачивает image оттуда.

Примеры:

```text
Docker Hub
GHCR
GitLab Container Registry
Harbor
AWS ECR
GCP Artifact Registry
Yandex Container Registry
```

Связано с [[Docker Image]], [[CI-CD]], [[GHCR]], [[GitLab Container Registry]], [[Harbor]].

---

# Что хранит registry

Registry хранит:

```text
manifests
layers
tags
digests
multi-arch indexes
signatures/attestations если настроены
```

Image layer может переиспользоваться несколькими tags.

---

# Login, push, pull

Login:

```bash
docker login registry.example.com
```

Tag:

```bash
docker tag app:dev registry.example.com/team/app:1.0.0
```

Push:

```bash
docker push registry.example.com/team/app:1.0.0
```

Pull:

```bash
docker pull registry.example.com/team/app:1.0.0
```

---

# Tags

Хорошие tags:

```text
1.4.2
1.4.2-build.17
main-a1b2c3d
sha-a1b2c3d
```

Опасный tag:

```text
latest
```

`latest` не означает “самый новый”. Это просто tag, который кто-то поставил.

---

# Digest

Digest указывает на конкретный content:

```text
registry.example.com/team/app@sha256:...
```

Для точного deploy лучше фиксировать digest, особенно если tag может быть перезаписан.

Проверить digest:

```bash
docker inspect --format='{{index .RepoDigests 0}}' registry.example.com/team/app:1.0.0
```

---

# Registry в CI/CD

Обычная цепочка:

```text
build image
scan image
push image
deploy tag/digest
```

Важно:

```text
не пушить из feature branch в production tag
не использовать shared credentials без нужды
чистить старые tags retention policy
сканировать images
```

---

# Auth

Варианты:

```text
username/password
personal access token
deploy token
cloud IAM
OIDC federation
robot account
```

В CI лучше использовать short-lived credentials или OIDC, если registry это поддерживает.

---

# Частые проблемы

## pull access denied

Причины:

```text
неверный registry path
нет login
нет прав на repository
image tag не существует
```

---

## manifest unknown

Tag отсутствует или ещё не запушен.

Проверить exact tag в CI logs.

---

## no matching manifest for linux/arm64

Image не собран под нужную architecture.

Нужен multi-platform build через [[BuildKit]].

---

# Связанные заметки

- [[Docker Image]]
- [[BuildKit]]
- [[Image Security]]
- [[CI-CD]]
- [[GHCR]]
- [[GitLab Container Registry]]
- [[Harbor]]

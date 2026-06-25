# BuildKit

`BuildKit` — современный backend для сборки Docker images.

Он ускоряет сборки, лучше работает с cache, поддерживает secret mounts, SSH mounts, parallel build graph и расширенный output.

Связан с [[Dockerfile]], [[Docker Image]], [[Multi-stage Build]], [[CI-CD]].

---

# Включить BuildKit

В современных Docker версиях BuildKit обычно уже включён.

Явно:

```bash
DOCKER_BUILDKIT=1 docker build -t app:dev .
```

Через buildx:

```bash
docker buildx build -t app:dev .
```

---

# Cache mount

Cache mount ускоряет package managers.

Пример npm:

```dockerfile
RUN --mount=type=cache,target=/root/.npm npm ci
```

Пример apt:

```dockerfile
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y curl
```

Cache не попадает в final image как обычный layer content.

---

# Secret mount

Secret mount даёт использовать secret во время build, не записывая его в image layer.

Dockerfile:

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

Build:

```bash
docker build --secret id=npmrc,src=$HOME/.npmrc -t app:dev .
```

Это лучше, чем `ARG TOKEN`, потому что `ARG` может засветиться в history/layers/logs.

---

# SSH mount

Нужен, если во время build надо скачать private git dependency.

```dockerfile
RUN --mount=type=ssh git clone git@github.com:org/private-repo.git
```

Build:

```bash
docker build --ssh default -t app:dev .
```

---

# buildx

`docker buildx` — CLI для BuildKit builders.

Проверить builders:

```bash
docker buildx ls
```

Создать builder:

```bash
docker buildx create --use --name builder
```

Multi-platform build:

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t registry.example.com/app:1.0.0 \
  --push .
```

---

# Cache в CI

Пример registry cache:

```bash
docker buildx build \
  --cache-from type=registry,ref=registry.example.com/app:buildcache \
  --cache-to type=registry,ref=registry.example.com/app:buildcache,mode=max \
  -t registry.example.com/app:sha-abc123 \
  --push .
```

Это полезно для ephemeral CI runners, где local cache исчезает после job.

---

# Частые проблемы

## Secret не найден

Проверить id:

```text
Dockerfile id=npmrc
docker build --secret id=npmrc,src=...
```

---

## Cache не используется

Причины:

```text
изменился COPY до RUN
разный build context
не настроен cache-from/cache-to в CI
не тот builder
```

---

## Multi-platform build падает

Причины:

```text
base image не поддерживает platform
зависимость скачивает бинарь не той архитектуры
QEMU медленный или не настроен
```

---

# Связанные заметки

- [[Dockerfile]]
- [[Docker Image]]
- [[Multi-stage Build]]
- [[CI Build Cache]]
- [[Secrets in CI-CD]]

# Docker Image

`Docker Image` — неизменяемый шаблон файловой системы и metadata, из которого запускают containers.

Image содержит:

```text
filesystem layers
config
environment defaults
entrypoint/cmd
labels
exposed ports metadata
```

Image создаётся из [[Dockerfile]] и обычно публикуется в [[Container Registry]].

---

# Image vs container

Image:

```text
read-only template
```

Container:

```text
running/stopped process + writable layer
```

Пример:

```bash
docker pull nginx:1.27
docker run -d --name web nginx:1.27
```

`nginx:1.27` — image.

`web` — container.

---

# Layers

Image состоит из layers.

Layers переиспользуются между images.

Плюсы:

```text
быстрее pull/push
лучше build cache
меньше места при общих base layers
```

Посмотреть:

```bash
docker history nginx:1.27
docker image inspect nginx:1.27
```

---

# Tag и digest

Tag:

```text
myapp:1.4.2
myapp:main
myapp:latest
```

Tag — имя, которое может быть перезаписано.

Digest:

```text
myapp@sha256:...
```

Digest указывает на конкретный immutable content.

Для production deploy лучше хранить, какой digest реально задеплоен.

---

# Сборка

```bash
docker build -t registry.example.com/team/app:1.0.0 .
```

С несколькими тегами:

```bash
docker build \
  -t registry.example.com/team/app:1.0.0 \
  -t registry.example.com/team/app:latest \
  .
```

Push:

```bash
docker push registry.example.com/team/app:1.0.0
```

---

# Что должно быть в хорошем image

```text
только runtime dependencies
нет build tools без необходимости
нет secrets
не root user
понятный ENTRYPOINT/CMD
минимальная attack surface
labels с source/revision
healthcheck если он уместен
```

---

# Проверка image

Список images:

```bash
docker images
```

Inspect:

```bash
docker image inspect app:1.0.0
```

История:

```bash
docker history --no-trunc app:1.0.0
```

Размер:

```bash
docker images app
```

---

# Частые проблемы

## Image слишком большой

Причины:

```text
build artifacts остались в runtime
package manager cache не очищен
COPY . . тащит лишнее
нет .dockerignore
```

Решение: [[Multi-stage Build]], `.dockerignore`, slim/distroless base.

---

## Image не воспроизводится

Причины:

```text
latest tags
unpinned dependencies
apt-get install без версии
скачивание файлов без checksum
```

---

## В image попали secrets

Проверять:

```bash
docker history --no-trunc image
docker save image -o image.tar
```

---

# Связанные заметки

- [[Docker]]
- [[Dockerfile]]
- [[Multi-stage Build]]
- [[Container Registry]]
- [[Image Security]]

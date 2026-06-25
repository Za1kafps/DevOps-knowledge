# Dockerfile

`Dockerfile` — файл с инструкциями для сборки [[Docker Image]].

Он описывает:

```text
base image
system packages
working directory
dependencies
application files
build commands
runtime command
user
ports/metadata
```

Dockerfile связан с [[Multi-stage Build]], [[BuildKit]], [[Image Security]] и [[Container Security]].

---

# Минимальный пример

```dockerfile
FROM alpine:3.20
WORKDIR /app
COPY app.sh .
RUN chmod +x app.sh
CMD ["./app.sh"]
```

Сборка:

```bash
docker build -t myapp:dev .
```

Запуск:

```bash
docker run --rm myapp:dev
```

---

# Важные инструкции

## FROM

Base image.

```dockerfile
FROM debian:12-slim
```

Лучше фиксировать версии, а не использовать `latest`.

---

## WORKDIR

Рабочая директория внутри image.

```dockerfile
WORKDIR /app
```

---

## COPY

Копирует файлы из build context.

```dockerfile
COPY package.json package-lock.json ./
```

---

## RUN

Выполняется во время сборки image.

```dockerfile
RUN apt-get update && apt-get install -y curl
```

Важно чистить package cache, если base image не делает это сам.

---

## CMD и ENTRYPOINT

`CMD` — команда по умолчанию.

`ENTRYPOINT` — основной executable контейнера.

Частый production-вариант:

```dockerfile
ENTRYPOINT ["/app/server"]
```

---

# Build context

Build context — директория, которую Docker отправляет builder.

Если в context попали `.git`, logs, secrets, `node_modules`, сборка будет медленнее и опаснее.

Используй `.dockerignore`:

```text
.git
node_modules
*.log
.env
dist
```

---

# Layers

Каждая инструкция создаёт layer или metadata.

Порядок инструкций влияет на cache.

Хорошо:

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
```

Плохо:

```dockerfile
COPY . .
RUN npm ci
```

Во втором случае любое изменение исходников ломает cache dependencies.

---

# Multi-stage

Для compiled languages лучше разделять build и runtime:

```dockerfile
FROM golang:1.22-alpine AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app ./cmd/app

FROM alpine:3.20
RUN adduser -D app
USER app
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

Смотри [[Multi-stage Build]].

---

# Secrets

Нельзя делать так:

```dockerfile
ARG TOKEN
RUN curl -H "Authorization: Bearer $TOKEN" ...
```

Secret может попасть в layer history.

С BuildKit используй secret mount:

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

Смотри [[BuildKit]].

---

# Проверка

Собрать:

```bash
docker build -t app:dev .
```

Посмотреть history:

```bash
docker history app:dev
```

Запустить:

```bash
docker run --rm app:dev
```

Проверить пользователя:

```bash
docker run --rm app:dev id
```

---

# Частые ошибки

## Файл не найден при COPY

Файл не входит в build context или исключён `.dockerignore`.

## `latest` неожиданно изменился

Base image обновился, сборка стала другой.

Используй version tag или digest для критичных окружений.

## Secret попал в image

Проверяй `docker history`, layers и CI logs.

---

# Связанные заметки

- [[Docker]]
- [[Docker Image]]
- [[Multi-stage Build]]
- [[BuildKit]]
- [[Image Security]]

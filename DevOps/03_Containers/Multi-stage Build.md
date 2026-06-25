# Multi-stage Build

`Multi-stage build` — способ собирать Docker image в несколько этапов.

Идея:

```text
build stage содержит compiler, dev dependencies и tools
runtime stage содержит только то, что нужно для запуска
```

Это уменьшает image, снижает attack surface и не тащит build artifacts в production.

---

# Пример Go

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

Что происходит:

```text
golang image используется только для сборки
в runtime попадает только бинарник /app
```

---

# Пример Node.js

```dockerfile
FROM node:22-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:22-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

---

# Именованные stages

Stage можно назвать:

```dockerfile
FROM golang:1.22 AS build
```

И копировать из него:

```dockerfile
COPY --from=build /out/app /app
```

Это лучше, чем ссылаться на номер stage.

---

# Сборка конкретного stage

Полезно для debug:

```bash
docker build --target build -t app:build .
```

Можно зайти внутрь:

```bash
docker run --rm -it app:build sh
```

---

# Что не надо делать

Не копируй всё из build stage:

```dockerfile
COPY --from=build / /
```

Так можно случайно утащить compiler, cache, credentials, temp files.

Копируй конкретные артефакты:

```dockerfile
COPY --from=build /out/app /app
```

---

# Польза

```text
меньше image size
меньше CVE в runtime image
быстрее pull/deploy
лучше separation build/runtime
секреты и caches проще не протащить дальше
```

---

# Частые ошибки

## Бинарник не запускается в runtime

Причины:

```text
нет libc
CGO включён
не хватает shared libraries
architecture mismatch
```

Проверить:

```bash
ldd ./app
file ./app
```

---

## Неправильный path в COPY --from

Проверять stage через:

```bash
docker build --target build -t debug .
docker run --rm -it debug sh
```

---

# Связанные заметки

- [[Dockerfile]]
- [[Docker Image]]
- [[BuildKit]]
- [[Distroless Images]]
- [[Image Security]]

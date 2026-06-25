# Build

`Build` — этап CI, где исходный код превращается в artifact.

Artifact может быть:

```text
binary
jar/war
npm package
python wheel
container image
static frontend bundle
helm chart
```

Build относится к [[Continuous Integration]] и должен быть воспроизводимым.

---

# Что важно

Хороший build отвечает:

```text
из какого commit собран artifact
какие dependencies использованы
какая version/tag получилась
где artifact опубликован
как повторить сборку
```

Если невозможно понять, что именно задеплоено, build process плохой.

---

# Примеры

Go:

```bash
go test ./...
CGO_ENABLED=0 go build -o bin/app ./cmd/app
```

Node.js:

```bash
npm ci
npm test
npm run build
```

Docker image:

```bash
docker build -t registry.example.com/app:$GIT_SHA .
docker push registry.example.com/app:$GIT_SHA
```

---

# Build metadata

Полезно вшивать:

```text
version
git commit
build time
branch/tag
```

Пример Go:

```bash
go build -ldflags "-X main.version=$GIT_SHA" -o app ./cmd/app
```

---

# Частые ошибки

## Build зависит от локального состояния

Например, файл есть на laptop, но не коммитится в Git.

## Dependencies не зафиксированы

Нет lockfile или версии плавают.

## Tests идут не от того artifact

Сначала тестируют одно, потом собирают другое.

## Artifact не публикуется

Pipeline зелёный, но deploy берёт неизвестно что.

---

# Связанные заметки

- [[Continuous Integration]]
- [[Artifacts and Cache]]
- [[Docker Image]]
- [[Dockerfile]]
- [[CI Build Cache]]

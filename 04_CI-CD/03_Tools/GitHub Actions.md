# GitHub Actions

`GitHub Actions` — CI/CD система GitHub, где workflow описывается YAML-файлами в `.github/workflows`.

Используется для:

```text
tests
build
container image publish
release automation
deploy
security scans
scheduled jobs
```

---

# Основные сущности

```text
workflow  файл и весь процесс
event     push, pull_request, tag, schedule
job       набор steps
step      команда или action
runner    среда выполнения
artifact  сохранённый результат
secret    секрет
environment protected target
```

---

# Пример CI

```yaml
name: ci

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go test ./...
```

---

# Publish image to GHCR

```yaml
permissions:
  contents: read
  packages: write

jobs:
  image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - run: |
          docker build -t ghcr.io/org/app:${{ github.sha }} .
          docker push ghcr.io/org/app:${{ github.sha }}
```

---

# Security model

Важно настраивать `permissions`.

Не давай workflow лишний доступ:

```yaml
permissions:
  contents: read
```

Для cloud deploy лучше использовать [[OIDC in CI-CD]], а не long-lived cloud keys.

---

# Частые проблемы

## Secrets недоступны в pull_request from fork

Это защита от утечки secrets.

## Неправильные permissions

Job не может push package или получить OIDC token.

## latest runner image изменился

`ubuntu-latest` может обновляться. Для строгой воспроизводимости фиксируй versions tools/actions.

---

# Связанные заметки

- [[CI-CD]]
- [[GitHub Actions Secrets]]
- [[GHCR]]
- [[OIDC in CI-CD]]
- [[Pipeline Rules]]

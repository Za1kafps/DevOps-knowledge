# GitHub Actions Secrets

`GitHub Actions Secrets` — encrypted values, доступные workflow во время выполнения.

Secrets могут быть на уровнях:

```text
repository
environment
organization
```

---

# Как использовать

```yaml
steps:
  - run: curl -H "Authorization: Bearer $TOKEN" https://api.example.com
    env:
      TOKEN: ${{ secrets.API_TOKEN }}
```

Не выводи secrets в logs.

---

# Environment secrets

Environment secrets полезны для production:

```text
environment: production
required reviewers
deployment branches
secrets only for prod job
```

Так production secret не доступен обычному test job.

---

# GITHUB_TOKEN

`GITHUB_TOKEN` создаётся автоматически для workflow.

Его права задаются через:

```yaml
permissions:
  contents: read
  packages: write
```

Лучше явно задавать permissions, а не полагаться на defaults.

---

# OIDC вместо cloud keys

Для AWS/GCP/Azure лучше использовать short-lived credentials через [[OIDC in CI-CD]].

Так в GitHub не хранится долгоживущий cloud secret.

---

# Частые ошибки

## Secret попал в build arg

Docker build args могут светиться в history/layers.

Используй BuildKit secrets.

## Secret нужен в fork PR

GitHub не отдаёт secrets fork PR по умолчанию. Это нормально.

## Echo/debug

Осторожно с `set -x`, verbose clients и печатью env.

---

# Связанные заметки

- [[GitHub Actions]]
- [[Secrets in CI-CD]]
- [[OIDC in CI-CD]]
- [[BuildKit]]

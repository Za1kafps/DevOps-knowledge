# OIDC in CI-CD

`OIDC in CI-CD` — способ дать pipeline short-lived credentials без хранения долгоживущих cloud keys в secrets.

Pipeline получает OIDC token от CI provider, cloud проверяет claims и выдаёт временные права.

---

# Зачем это нужно

Плохо:

```text
AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY лежат в CI secrets годами
```

Лучше:

```text
GitHub/GitLab issues OIDC token
cloud IAM trusts specific repo/branch/environment
pipeline gets temporary credentials
```

---

# Что проверять в claims

```text
repository/project
branch/tag
environment
workflow/pipeline source
audience
subject
```

Trust policy должна быть узкой.

---

# Где используют

```text
AWS IAM role assumption
GCP Workload Identity Federation
Azure federated credentials
Vault JWT/OIDC auth
```

---

# Частые ошибки

## Trust policy слишком широкая

Любая branch может получить production role.

## Не настроены permissions

Например в GitHub Actions нужен:

```yaml
permissions:
  id-token: write
  contents: read
```

## Audience mismatch

Cloud/Vault ждёт один audience, CI выдаёт другой.

---

# Связанные заметки

- [[Secrets in CI-CD]]
- [[GitHub Actions]]
- [[GitLab CI]]
- [[Vault]]
- [[Security]]

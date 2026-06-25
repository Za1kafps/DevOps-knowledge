# Vault

`Vault` — система управления secrets и выдачи динамических credentials.

Vault нужен, когда secrets нельзя хранить в plaintext, env-файлах и CI variables без контроля lifecycle.

---

# Что умеет

```text
KV secrets
dynamic database credentials
PKI certificates
cloud credentials
transit encryption
leases and revocation
audit logs
policy-based access
```

---

# Основные понятия

```text
auth method
policy
token
secret engine
lease
renew
revoke
audit device
```

---

# KV пример

```bash
vault kv put secret/app DATABASE_URL=postgres://...
vault kv get secret/app
```

Policy:

```hcl
path "secret/data/app" {
  capabilities = ["read"]
}
```

---

# Dynamic DB credentials

Вместо одного вечного DB password Vault может выдавать временного пользователя.

Плюсы:

```text
short-lived access
revocation
audit trail
least privilege
```

---

# Production важное

```text
unseal/recovery процесс
HA storage
audit logs включены
policies минимальны
root token не используется
backup storage backend
monitoring seals/leader/latency
```

---

# Частые проблемы

## Vault sealed

Приложения не могут получить secrets.

## Token expired

Нужен renew или auth method с корректным lifecycle.

## Policy слишком широкая

`path "*"` с `sudo` — почти root.

---

# Связанные заметки

- [[Secrets Management]]
- [[OIDC in CI-CD]]
- [[Database TLS]]
- [[Audit Logs]]
- [[Security]]

# Secrets Management

`Secrets Management` — хранение, выдача, ротация и аудит секретов.

Secret — это всё, что даёт доступ:

```text
password
API token
private key
TLS key
database credentials
cloud credentials
JWT signing key
```

---

# Где secrets не должны жить

```text
Git plaintext
Docker image layers
CI logs
Slack messages
wiki pages
local .env без контроля
Terraform state без защиты
```

---

# Хорошая модель

```text
central secret storage
least privilege
short-lived credentials где возможно
rotation
audit logs
separation by environment
break-glass process
```

---

# Инструменты

```text
Vault
cloud secret managers
SOPS
Sealed Secrets
External Secrets Operator
Kubernetes Secrets with encryption at rest
CI protected secrets
```

---

# Ротация

Для каждого secret должно быть понятно:

```text
где используется
кто владелец
как заменить
как проверить
как откатить
как часто ротировать
```

---

# Частые ошибки

## Нет inventory secrets

Никто не знает, что сломается при rotation.

## Один secret на dev/stage/prod

Компрометация dev даёт доступ к prod.

## Secret попал в image

Проверять `docker history`, layers и build logs.

---

# Связанные заметки

- [[Vault]]
- [[SOPS]]
- [[Sealed Secrets]]
- [[Secrets in CI-CD]]
- [[Kubernetes Security]]

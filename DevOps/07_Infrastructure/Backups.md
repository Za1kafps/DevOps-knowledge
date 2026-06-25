# Backups

`Backups` в infrastructure — копии данных и конфигураций, нужные для восстановления.

Backup должен быть внешним по отношению к отказавшей системе.

---

# Что бэкапить

```text
databases
object storage critical data
Terraform state
Kubernetes manifests/secrets strategy
Vault storage/backend
server configs
CI/CD configs
```

---

# Правило 3-2-1

```text
3 copies
2 different media/storage types
1 offsite/off-account
```

Для cloud важно думать не только о регионе, но и об аккаунте/IAM compromise.

---

# Проверка

```text
backup job status
backup age
backup size
checksum
restore drill result
retention policy
```

---

# Частые ошибки

```text
backup на том же диске
нет restore drill
нет encryption
нет monitoring backup failures
retention удаляет нужную точку
```

---

# Связанные заметки

- [[Database Backups]]
- [[Backup Strategy]]
- [[Disaster Recovery]]
- [[RTO and RPO]]

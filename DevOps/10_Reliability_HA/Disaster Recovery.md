# Disaster Recovery

`Disaster Recovery` — план восстановления после крупной аварии.

DR нужен, когда обычный restart/rollback не помогает:

```text
потеря базы
потеря региона
corrupted data
удаление cluster
компрометация аккаунта
массовая ошибка deploy
```

---

# Что должно быть в DR plan

```text
RTO/RPO
критичные сервисы
backup locations
restore steps
access requirements
DNS/failover steps
communication plan
validation checklist
owners
```

---

# Restore order

Обычно:

```text
network/IAM
databases/storage
secrets
Kubernetes/control plane
platform services
applications
DNS/traffic
validation
```

Порядок зависит от архитектуры, но он должен быть записан.

---

# DR drill

DR plan без drill почти всегда врёт.

Проверять:

```text
можем ли получить доступ?
backup читается?
restore укладывается в RTO?
данные укладываются в RPO?
приложение стартует на восстановленных данных?
```

---

# Частые ошибки

## Backup в том же аккаунте без защиты

Компрометация аккаунта удаляет и production, и backup.

## Нет secrets restore

Инфраструктура поднялась, приложения не могут получить credentials.

## DNS TTL слишком большой

Failover технически готов, но клиенты долго идут в старое место.

---

# Связанные заметки

- [[RTO and RPO]]
- [[Backup Strategy]]
- [[Database Restore Drill]]
- [[Incident Response Flow]]

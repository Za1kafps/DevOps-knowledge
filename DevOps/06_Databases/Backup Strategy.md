# Backup Strategy

`Backup Strategy` описывает что, как часто, куда и как долго бэкапится.

---

# Что определить

```text
RPO/RTO
backup type
schedule
retention
storage location
encryption
restore drill frequency
owners
alerts
```

---

# Хорошая стратегия

```text
daily logical backups
continuous WAL archive для PITR
offsite/off-account storage
encryption at rest
retention by policy
regular restore drills
monitoring backup freshness
```

---

# Anti-patterns

```text
backup на том же сервере
нет restore test
нет alert если backup не создался
неизвестно кто владелец
retention удаляет нужные точки
```

---

# Связанные заметки

- [[Database Backups]]
- [[Database Restore Drill]]
- [[RTO and RPO]]
- [[Disaster Recovery]]

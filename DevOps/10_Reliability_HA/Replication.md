# Replication

`Replication` — копирование данных или состояния между узлами.

Replication нужна для read scaling, HA и disaster recovery, но не заменяет backup.

---

# Sync vs async

Synchronous:

```text
меньше риск потери данных
выше latency
primary зависит от replica
```

Asynchronous:

```text
ниже latency
есть replication lag
можно потерять последние writes при failover
```

---

# Что смотреть

```text
lag
quorum
consistency model
failover behavior
split-brain protection
backpressure на primary
```

---

# Replication не backup

Если удалить данные на primary, replication может быстро удалить их и на replica.

Backup нужен отдельно.

---

# Связанные заметки

- [[PostgreSQL Replication]]
- [[Redis Sentinel]]
- [[High Availability]]
- [[Backup Strategy]]

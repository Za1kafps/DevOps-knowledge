# TarantoolDB

`Tarantool` — in-memory database/application server с Lua runtime.

---

# Где встречается

```text
low-latency storage
queues
cache with logic
high-throughput services
```

---

# Что важно

```text
memory usage
snapshots
WAL/xlog
replication lag
vshard если используется
backup/restore
```

---

# Проверка

Через console/admin tooling смотреть:

```text
box.info()
box.slab.info()
box.cfg
replication status
```

---

# Частые проблемы

```text
memory exhausted
replication lag
snapshot не создаётся
disk full из-за xlog
schema/data migration без rollback
```

---

# Связанные заметки

- [[Databases]]
- [[Backup Strategy]]
- [[Replication]]

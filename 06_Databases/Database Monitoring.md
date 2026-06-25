# Database Monitoring

`Database Monitoring` показывает здоровье БД до того, как пользователи заметят деградацию.

---

# Что мониторить

```text
availability
connections
active/idle/idle in transaction
slow queries
locks
replication lag
disk usage
WAL growth
cache hit ratio
IO latency
backup freshness
```

---

# PostgreSQL queries

Connections:

```sql
select state, count(*) from pg_stat_activity group by state;
```

Locks:

```sql
select locktype, mode, granted, count(*) from pg_locks group by locktype, mode, granted;
```

Replication:

```sql
select application_name, state, replay_lag from pg_stat_replication;
```

---

# Alerts

```text
disk will fill soon
replication lag high
too many connections
backup missing/stale
database down
long transaction
```

---

# Связанные заметки

- [[PostgreSQL]]
- [[Prometheus]]
- [[Alerting Rules]]
- [[Database Backups]]

# PostgreSQL Replication

PostgreSQL replication передаёт WAL с primary на standby.

Используется для:

```text
read replicas
high availability
failover
backup offloading
PITR pipelines
```

---

# Streaming replication

Standby подключается к primary и получает WAL stream.

На primary:

```sql
select application_name, state, sync_state, write_lag, flush_lag, replay_lag
from pg_stat_replication;
```

На standby:

```sql
select pg_is_in_recovery();
select now() - pg_last_xact_replay_timestamp() as replay_delay;
```

---

# Sync vs async

Async:

```text
меньше latency
можно потерять последние transactions при failover
```

Sync:

```text
меньше риск потери данных
выше latency/зависимость от replica
```

---

# Replication slots

Slot удерживает WAL, пока replica/consumer его не прочитает.

Проверка:

```sql
select slot_name, active, restart_lsn
from pg_replication_slots;
```

Inactive slot может заполнить disk через pg_wal.

---

# Частые проблемы

## replication lag

Причины: network, slow standby disk, heavy queries on replica, WAL burst.

## failover без fencing

Можно получить split-brain.

## read-after-write inconsistency

Async replica может отставать, пользователь не видит только что записанные данные.

---

# Связанные заметки

- [[PostgreSQL]]
- [[WAL]]
- [[Failover]]
- [[RTO and RPO]]

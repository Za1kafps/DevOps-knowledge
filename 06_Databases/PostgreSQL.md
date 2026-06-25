# PostgreSQL

`PostgreSQL` — реляционная БД, которую DevOps чаще всего трогает через доступность, backup/restore, connections, replication, WAL, disk и monitoring.

Postgres — stateful-система. Главный вопрос не “как запустить”, а:

```text
как не потерять данные
как восстановиться
как понять причину деградации
как безопасно обновить schema
```

---

# Базовая проверка

```bash
pg_isready -h localhost -p 5432
psql -U postgres -c "select version();"
psql -c "select now();"
```

Активные connections:

```sql
select state, count(*)
from pg_stat_activity
group by state;
```

Долгие запросы:

```sql
select pid, now() - query_start as age, state, query
from pg_stat_activity
where state <> 'idle'
order by age desc;
```

---

# Где лежат данные

Путь зависит от установки.

Узнать:

```sql
show data_directory;
```

Внутри важны:

```text
base/        данные таблиц
pg_wal/      WAL
pg_tblspc/   tablespaces
postgresql.conf
pg_hba.conf
```

Не делай backup простым `cp -r` live data directory без понимания consistency.

---

# WAL

[[WAL]] — Write-Ahead Log.

Postgres сначала пишет изменения в WAL, потом в data files.

WAL нужен для:

```text
crash recovery
replication
PITR
backup consistency
```

Если `pg_wal` разросся, часто проблема в replication slot, archiving или долгом backup.

---

# Connections

Проверить лимит:

```sql
show max_connections;
```

Активность:

```sql
select usename, application_name, client_addr, state, count(*)
from pg_stat_activity
group by usename, application_name, client_addr, state
order by count desc;
```

Если много short-lived connections, нужен [[PgBouncer]].

---

# Backup

Logical backup:

```bash
pg_dump -Fc appdb -f appdb.dump
pg_restore -l appdb.dump | head
```

Physical backup:

```bash
pg_basebackup -D /backup/base -Ft -z -P
```

Смотри [[pg_dump and pg_restore]], [[pg_basebackup]], [[Database Backups]].

---

# Replication

На primary:

```sql
select application_name, state, sync_state, write_lag, flush_lag, replay_lag
from pg_stat_replication;
```

Replication lag важен для read replicas и failover.

---

# Частые проблемы

## connection refused

Postgres не слушает host/port, firewall, `listen_addresses`, container port, Service.

## too many connections

Нет pooling, leak connections, слишком маленький max_connections.

## disk full

Проверить data dir, WAL, indexes, temp files.

## slow queries

Смотреть indexes, locks, query plans, vacuum, IO.

---

# Связанные заметки

- [[WAL]]
- [[PostgreSQL Replication]]
- [[PgBouncer]]
- [[Database Backups]]
- [[Database Migrations]]
- [[PostgreSQL Too Many Connections]]
- [[PostgreSQL connection refused]]

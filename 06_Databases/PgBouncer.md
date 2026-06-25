# PgBouncer

`PgBouncer` — lightweight connection pooler для PostgreSQL.

Он нужен, когда приложение создаёт много connections, а Postgres не должен держать тысячи backend processes.

---

# Зачем нужен

PostgreSQL connection — дорогой процесс.

Если много приложений/Pod-ов открывают connections напрямую:

```text
max_connections быстро заканчивается
растёт memory usage
увеличивается context switching
DB деградирует
```

PgBouncer держит меньше реальных connections к PostgreSQL и переиспользует их.

---

# Pool modes

## Session pooling

Connection закреплён за client на всю session.

Максимальная совместимость, меньше выгоды.

---

## Transaction pooling

Connection возвращается в pool после transaction.

Самый частый режим для web workloads.

Ограничения:

```text
session state
prepared statements
temporary tables
LISTEN/NOTIFY
```

---

## Statement pooling

Connection возвращается после statement.

Используется редко из-за ограничений.

---

# Проверка

Подключиться к admin console:

```bash
psql -h pgbouncer -p 6432 pgbouncer
```

Команды:

```sql
show pools;
show clients;
show servers;
show stats;
```

---

# Настройки

Ключевые:

```text
pool_mode
max_client_conn
default_pool_size
reserve_pool_size
server_idle_timeout
query_timeout
```

---

# Частые проблемы

## Приложение ломается в transaction pooling

Оно использует session-level features.

## Pool слишком маленький

Запросы ждут server connection.

## Pool слишком большой

PgBouncer перестаёт защищать PostgreSQL.

---

# Связанные заметки

- [[PostgreSQL]]
- [[Connection Pool]]
- [[PostgreSQL Too Many Connections]]
- [[Database Monitoring]]

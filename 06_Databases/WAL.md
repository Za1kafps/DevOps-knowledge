# WAL

`WAL` — Write-Ahead Log в PostgreSQL.

Postgres сначала пишет изменение в WAL, и только потом оно попадает в data files.

Это нужно, чтобы после crash восстановить согласованное состояние.

---

# Зачем WAL нужен

```text
crash recovery
replication
point-in-time recovery
backup consistency
logical decoding
```

Без WAL Postgres не смог бы безопасно переживать падение процесса/сервера.

---

# Где лежит

Обычно внутри data directory:

```text
pg_wal/
```

Узнать data dir:

```sql
show data_directory;
```

---

# Проверка WAL

Текущий LSN:

```sql
select pg_current_wal_lsn();
```

Replication slots:

```sql
select slot_name, slot_type, active, restart_lsn
from pg_replication_slots;
```

Archiving:

```sql
select * from pg_stat_archiver;
```

---

# Почему pg_wal растёт

Частые причины:

```text
replica отстала
replication slot удерживает WAL
archive_command падает
долгий backup
очень много writes
```

Проверить inactive slots:

```sql
select slot_name, active, restart_lsn
from pg_replication_slots;
```

---

# WAL и backup

Для PITR нужен base backup + archived WAL.

```text
base backup = состояние на момент времени
WAL archive = изменения после base backup
```

Restore без нужных WAL сможет восстановиться только до состояния base backup.

---

# Опасные действия

Нельзя просто удалять файлы из `pg_wal`, чтобы освободить место.

Это может сломать recovery/replication и привести к потере данных.

Надо найти причину удержания WAL.

---

# Связанные заметки

- [[PostgreSQL]]
- [[PostgreSQL Replication]]
- [[pg_basebackup]]
- [[Database Backups]]
- [[Disaster Recovery]]

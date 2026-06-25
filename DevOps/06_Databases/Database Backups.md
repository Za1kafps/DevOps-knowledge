# Database Backups

Database backup — копия данных, из которой можно восстановить сервис.

Backup считается настоящим только после успешного restore test.

---

# Виды backup

## Logical backup

Экспорт SQL/object-level.

PostgreSQL:

```bash
pg_dump -Fc appdb -f appdb.dump
```

Плюсы:

```text
удобно переносить между версиями
можно восстановить отдельные objects
легче inspect
```

Минусы:

```text
медленнее на больших базах
restore может быть долгим
не всегда подходит для PITR
```

---

## Physical backup

Копия data files в согласованном виде.

PostgreSQL:

```bash
pg_basebackup -D /backup/base -Ft -z -P
```

Плюсы:

```text
быстрее для больших баз
подходит для PITR с WAL
можно поднимать replica
```

Минусы:

```text
больше привязка к версии/кластеру
сложнее точечный restore
```

---

# Что обязательно хранить

```text
backup file/object
timestamp
database version
schema/application version
encryption info
retention
checksum
restore procedure
```

---

# Проверка backup

PostgreSQL custom dump:

```bash
pg_restore -l appdb.dump | head
```

Restore в тестовую БД:

```bash
createdb restore_test
pg_restore -d restore_test appdb.dump
```

Проверка данных:

```sql
select count(*) from important_table;
```

---

# Retention

Retention должен соответствовать RPO/RTO и юридическим требованиям.

Пример:

```text
daily backups 14 days
weekly backups 8 weeks
monthly backups 12 months
WAL archive 7 days
```

---

# Частые ошибки

## Backup есть, restore не проверялся

Самая частая и самая дорогая ошибка.

## Backup лежит на том же диске

При потере сервера теряется и backup.

## Нет encryption

Backup часто содержит все production данные.

## Нет monitoring backup job

Backup падает неделю, все узнают во время аварии.

---

# Связанные заметки

- [[Backup Strategy]]
- [[Database Restore Drill]]
- [[PostgreSQL]]
- [[pg_dump and pg_restore]]
- [[pg_basebackup]]
- [[RTO and RPO]]

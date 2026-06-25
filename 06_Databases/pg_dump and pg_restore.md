# pg_dump and pg_restore

`pg_dump` делает logical backup PostgreSQL.

`pg_restore` восстанавливает dump, если dump создан в custom/directory/tar format.

---

# Custom format

Создать backup:

```bash
pg_dump -Fc -d appdb -f appdb.dump
```

Посмотреть содержимое:

```bash
pg_restore -l appdb.dump | head
```

Восстановить:

```bash
createdb appdb_restore
pg_restore -d appdb_restore appdb.dump
```

---

# Plain SQL

```bash
pg_dump -d appdb > appdb.sql
psql -d appdb_restore < appdb.sql
```

Plain SQL проще читать, но custom format гибче для restore.

---

# Важные флаги

```text
-Fc custom format
-Fd directory format
-j parallel jobs for restore/directory dump
--schema-only
--data-only
--no-owner
--no-privileges
```

---

# Проверка backup

Backup надо проверять restore-ом:

```bash
createdb restore_test
pg_restore -d restore_test appdb.dump
psql -d restore_test -c "select count(*) from important_table;"
```

---

# Частые ошибки

## Dump есть, restore не проверяли

Может оказаться битый файл, нет extensions, не хватает role/owner.

## Версии несовместимы

Обычно dump делают утилитой той же или более новой major версии, чем server.

## Нет глобальных objects

`pg_dump` не сохраняет roles/tablespaces. Для этого есть `pg_dumpall --globals-only`.

---

# Связанные заметки

- [[PostgreSQL]]
- [[Database Backups]]
- [[Database Restore Drill]]

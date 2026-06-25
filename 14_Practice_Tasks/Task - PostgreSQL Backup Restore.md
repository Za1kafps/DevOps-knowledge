# Task - PostgreSQL Backup Restore

## Цель

Создать logical backup, восстановить его в отдельную database и доказать целостность данных. Наличие backup-файла без restore drill не подтверждает возможность восстановления.

## Backup

Custom format:

```bash
pg_dump \
  --format=custom \
  --no-owner \
  --no-acl \
  --file=app.dump \
  "$DATABASE_URL"
```

Metadata:

```bash
sha256sum app.dump >app.dump.sha256
pg_restore --list app.dump >app.dump.list
```

## Restore

```bash
createdb app_restore
pg_restore \
  --dbname=app_restore \
  --clean \
  --if-exists \
  --no-owner \
  --exit-on-error \
  app.dump
```

Для parallel restore directory/custom format:

```bash
pg_restore --jobs=4 --dbname=app_restore app.dump
```

## Проверка

```bash
psql app_restore -c '\dt+'
psql app_restore -c 'SELECT count(*) FROM important_table;'
psql app_restore -c 'SELECT min(created_at), max(created_at) FROM important_table;'
```

Лучше иметь application-level invariants: количество активных объектов, контрольные суммы ключевых таблиц, успешный smoke test read-only API.

## Сценарии

1. Restore выполняется более новой/старой major version tools.
2. В target отсутствует extension.
3. Role/owner не существует.
4. На disk недостаточно места.
5. Backup сделан без large objects или части schemas.
6. Dump логически корректен, но RPO не выполняется.
7. Restore превышает RTO.

## Что записать

- время начала/окончания backup;
- размер и checksum;
- PostgreSQL/tool versions;
- encryption и место хранения;
- фактический RPO;
- фактическое restore time;
- результаты integrity checks.

## Связи

- [[Database Backups]]
- [[pg_dump and pg_restore]]
- [[Database Restore Drill]]
- [[RTO and RPO]]
- [[Backup Strategy]]

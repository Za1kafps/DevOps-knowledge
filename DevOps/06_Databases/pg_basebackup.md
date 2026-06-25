# pg_basebackup

`pg_basebackup` делает physical base backup PostgreSQL cluster.

Он копирует data directory в согласованном виде и используется для replicas и PITR-сценариев.

---

# Пример

```bash
pg_basebackup \
  -h primary.example.com \
  -U replication \
  -D /backup/base \
  -Ft -z -P \
  -X stream
```

Флаги:

```text
-D куда писать backup
-Ft tar format
-z compress
-P progress
-X stream WAL during backup
```

---

# Что нужно

```text
replication user
pg_hba.conf разрешает подключение
достаточно места
WAL доступен
network stable
```

---

# Проверка

```bash
tar -tf base.tar.gz | head
```

Но настоящая проверка — поднять test instance из backup.

---

# Частые проблемы

## replication permission denied

Пользователь не имеет REPLICATION или pg_hba запрещает.

## WAL missing

Нужен streamed WAL или archive для consistent recovery.

## backup не укладывается в окно

Нужно измерять throughput и размер базы.

---

# Связанные заметки

- [[PostgreSQL]]
- [[WAL]]
- [[Database Backups]]
- [[PostgreSQL Replication]]

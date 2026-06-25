# Databases

[[Databases]] — область DevOps про эксплуатацию stateful-систем.

Главное отличие от stateless-сервисов:

```text
контейнер можно пересоздать
данные нельзя просто пересоздать
```

Для DevOps база — это не только `docker run postgres`. Это backups, restore, replication, connection limits, migrations, TLS, monitoring, disk, latency и disaster recovery.

---

# Основные ветки

## PostgreSQL

- [[PostgreSQL]]
- [[WAL]]
- [[PostgreSQL Replication]]
- [[PgBouncer]]
- [[pg_dump and pg_restore]]
- [[pg_basebackup]]
- [[Transactions]]
- [[Indexes]]

---

## Redis

- [[Redis]]
- [[Redis Persistence]]
- [[Redis Sentinel]]
- [[Redis Cluster]]

Redis часто используют как cache, queue, rate limit storage и session storage. Ошибка persistence/eviction легко превращает cache в источник инцидентов.

---

## Object storage

- [[S3]]
- [[S3 Object Storage]]
- [[MinIO]]
- [[MinIO Operator]]
- [[Ceph]]
- [[Rook-Ceph]]
- [[Ceph OSD]]
- [[Ceph RGW]]

Object storage — не filesystem. У него другие consistency, listing, lifecycle и access patterns.

---

## Operations

- [[Database Backups]]
- [[Backup Strategy]]
- [[Database Restore Drill]]
- [[Database Migrations]]
- [[Database Monitoring]]
- [[Database TLS]]
- [[Connection Pool]]

---

# Что проверять в любой БД

```text
есть ли backup
проверялся ли restore
какой RPO/RTO
хватает ли disk
понятен ли connection limit
есть ли replication lag
есть ли TLS
какие slow queries
как проходят migrations
что будет при failover
```

---

# Базовые команды

PostgreSQL:

```bash
pg_isready -h localhost -p 5432
psql -c "select now();"
psql -c "select state,count(*) from pg_stat_activity group by state;"
```

Redis:

```bash
redis-cli ping
redis-cli info
redis-cli info replication
```

S3:

```bash
aws s3 ls s3://bucket/
aws s3api head-object --bucket bucket --key path/object
```

---

# Production правило

Backup без restore drill — это не backup, а надежда.

Monitoring без alerting — это dashboard decoration.

Replication без понимания lag — это не HA.

---

# Связанные заметки

- [[Reliability and High Availability]]
- [[Backup Strategy]]
- [[Disaster Recovery]]
- [[Observability]]
- [[Security]]

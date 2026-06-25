# MinIO

`MinIO` — S3-compatible object storage.

Используется для self-hosted object storage, backups, artifacts и локальных S3-compatible окружений.

---

# Проверка

Через `mc`:

```bash
mc alias set local http://minio:9000 ACCESS SECRET
mc ls local
mc admin info local
```

S3 API:

```bash
aws --endpoint-url http://minio:9000 s3 ls
```

---

# Production важное

```text
distributed mode
erasure coding
TLS
separate disks
monitoring
bucket policies
replication/lifecycle где нужно
backup для metadata/config
```

---

# Частые проблемы

```text
неверный endpoint/path-style
TLS certificate mismatch
disk offline
erasure set degraded
AccessDenied из-за policy
```

---

# Связанные заметки

- [[S3]]
- [[S3 Object Storage]]
- [[MinIO Operator]]
- [[Backups]]

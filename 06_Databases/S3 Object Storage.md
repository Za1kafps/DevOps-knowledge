# S3 Object Storage

`S3 Object Storage` — объектное хранилище, где данные лежат как objects в buckets.

Это не filesystem и не block storage.

Объект:

```text
bucket
key
metadata
content
version
etag/checksum
```

---

# Где используется

```text
backups
static files
logs archive
artifacts
database dumps
media files
Terraform state
```

---

# Основные операции

```bash
aws s3 ls s3://bucket/
aws s3 cp file.txt s3://bucket/path/file.txt
aws s3 sync ./dir s3://bucket/prefix/
aws s3api head-object --bucket bucket --key path/file.txt
```

---

# Важные свойства

```text
object key — не настоящий путь
rename = copy + delete
listing может быть дорогим на больших prefix
permissions через IAM/bucket policy
encryption отдельно настраивается
lifecycle rules удаляют/переносят objects
versioning защищает от случайного overwrite/delete
```

---

# Security

Проверять:

```text
public access block
bucket policy
IAM policy
server-side encryption
access logs/audit
versioning
```

---

# Частые проблемы

## AccessDenied

Проверить IAM, bucket policy, KMS key policy.

## Slow listing

Приложение использует object storage как filesystem.

## Удалили backup

Нужны versioning, object lock или retention policy.

---

# Связанные заметки

- [[S3]]
- [[MinIO]]
- [[Ceph RGW]]
- [[Database Backups]]
- [[Terraform]]

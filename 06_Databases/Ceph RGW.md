# Ceph RGW

`Ceph RGW` — RADOS Gateway, S3/Swift-compatible object gateway для Ceph.

---

# Где используется

```text
S3-compatible buckets
backup storage
artifact storage
multi-tenant object storage
```

---

# Проверка

```bash
ceph status
radosgw-admin user list
radosgw-admin bucket list
```

S3:

```bash
aws --endpoint-url https://rgw.example.com s3 ls
```

---

# Частые проблемы

```text
S3 auth/signature mismatch
bucket policy
RGW down
Ceph cluster degraded
TLS/proxy issue
```

---

# Связанные заметки

- [[Ceph]]
- [[S3]]
- [[S3 Object Storage]]

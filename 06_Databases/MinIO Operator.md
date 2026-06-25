# MinIO Operator

`MinIO Operator` управляет MinIO tenants в Kubernetes.

---

# Что важно

```text
tenant spec
storage class
number of servers/volumes
TLS
console/API endpoints
credentials
monitoring
```

---

# Проверка

```bash
kubectl get tenants -A
kubectl get pods -n minio-tenant
kubectl get pvc -n minio-tenant
kubectl logs -n minio-operator deploy/minio-operator
```

---

# Частые проблемы

```text
PVC Pending
tenant не Ready
TLS secret missing
диски разного размера
network policy blocking
```

---

# Связанные заметки

- [[MinIO]]
- [[S3 Object Storage]]
- [[PVC]]
- [[StorageClass]]

# CSI

`CSI` — Container Storage Interface.

Kubernetes использует CSI drivers для подключения внешних storage systems.

---

# Что делает CSI

```text
provision volume
attach volume to node
mount volume into Pod
resize volume
snapshot/clone если поддерживается
```

---

# Проверка

```bash
kubectl get csidriver
kubectl get pods -A | grep -i csi
kubectl describe pvc <pvc> -n <ns>
kubectl get events -n <ns> --sort-by=.lastTimestamp
```

---

# Частые проблемы

```text
provisioner down
attach timeout
node plugin не работает
нет прав cloud IAM
zone mismatch
volume limit на node
```

---

# Связанные заметки

- [[PVC]]
- [[PV]]
- [[StorageClass]]
- [[Rook-Ceph]]

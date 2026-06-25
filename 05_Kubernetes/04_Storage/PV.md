# PV

`PV` — PersistentVolume, объект Kubernetes, представляющий storage volume.

PVC запрашивает storage, PV предоставляет storage.

---

# Важные поля

```text
capacity
accessModes
storageClassName
reclaimPolicy
volumeMode
nodeAffinity
```

---

# Reclaim policy

```text
Retain  PV остаётся после удаления PVC
Delete  backend volume удаляется вместе с PVC
```

Для production данных `Delete` должен быть осознанным решением.

---

# Проверка

```bash
kubectl get pv
kubectl describe pv <pv>
kubectl get pvc -A
```

---

# Связанные заметки

- [[PVC]]
- [[StorageClass]]
- [[CSI]]
- [[Database Backups]]

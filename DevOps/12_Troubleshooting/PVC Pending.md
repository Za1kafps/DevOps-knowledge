# PVC Pending

`PVC Pending` означает, что PersistentVolumeClaim не получил volume.

---

# Проверка

```bash
kubectl get pvc -n app
kubectl describe pvc data -n app
kubectl get storageclass
kubectl get pv
kubectl get events -n app --sort-by=.lastTimestamp
```

---

# Частые причины

```text
storageClassName неверный
default StorageClass отсутствует
CSI provisioner не работает
access mode не поддерживается
нет capacity
volumeBindingMode WaitForFirstConsumer ждёт Pod
```

---

# CSI

Проверить storage controller:

```bash
kubectl get pods -A | grep -i csi
kubectl get csidriver
```

---

# Связанные заметки

- [[PVC]]
- [[PV]]
- [[StorageClass]]
- [[CSI]]
- [[Pod Pending]]

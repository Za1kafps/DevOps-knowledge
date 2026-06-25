# PVC

`PVC` — PersistentVolumeClaim, запрос Pod на persistent storage.

Pod не должен напрямую знать cloud disk/NFS/Ceph volume. Он просит storage через PVC.

```text
Pod -> PVC -> PV -> Storage backend
```

---

# Пример

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast
  resources:
    requests:
      storage: 20Gi
```

Использование в Pod:

```yaml
volumes:
  - name: data
    persistentVolumeClaim:
      claimName: data
```

---

# Access modes

```text
ReadWriteOnce   один node может mount read-write
ReadOnlyMany    много nodes read-only
ReadWriteMany   много nodes read-write
ReadWriteOncePod один Pod read-write
```

Поддержка зависит от storage backend.

---

# Проверка

```bash
kubectl get pvc -A
kubectl describe pvc data -n app
kubectl get pv
kubectl get storageclass
```

---

# Частые проблемы

## PVC Pending

Причины:

```text
нет StorageClass
storage provisioner не работает
нет свободного storage
access mode не поддерживается
volumeBindingMode ждёт Pod scheduling
```

## Pod не стартует из-за volume

Смотреть events Pod и PVC.

## Данные потерялись

Проверь reclaimPolicy PV и не удалили ли PVC.

---

# Связанные заметки

- [[PV]]
- [[StorageClass]]
- [[CSI]]
- [[PVC Pending]]
- [[Database Backups]]

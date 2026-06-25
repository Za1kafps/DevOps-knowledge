# StorageClass

`StorageClass` описывает тип dynamic provisioning storage.

PVC ссылается на StorageClass, а CSI provisioner создаёт volume.

---

# Проверка

```bash
kubectl get storageclass
kubectl describe storageclass <name>
```

---

# Важные поля

```text
provisioner
parameters
reclaimPolicy
volumeBindingMode
allowVolumeExpansion
```

`volumeBindingMode: WaitForFirstConsumer` откладывает создание volume до scheduling Pod. Это важно для zonal disks.

---

# Частые проблемы

```text
default StorageClass отсутствует
provisioner не работает
wrong zone
access mode не поддерживается
reclaimPolicy удаляет данные
```

---

# Связанные заметки

- [[PVC]]
- [[PV]]
- [[CSI]]
- [[PVC Pending]]

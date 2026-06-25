# Rook-Ceph

`Rook-Ceph` — Kubernetes operator для управления Ceph cluster.

---

# Что создаёт

```text
Ceph monitors
managers
OSDs
CSI drivers
StorageClasses
toolbox
RGW если настроен
```

---

# Проверка

```bash
kubectl -n rook-ceph get pods
kubectl -n rook-ceph get cephcluster
kubectl -n rook-ceph exec deploy/rook-ceph-tools -- ceph status
```

---

# Частые проблемы

```text
OSD не поднялся
диск уже содержит metadata
mon quorum lost
CSI provision failed
Ceph nearfull/full
```

---

# Связанные заметки

- [[Ceph]]
- [[Ceph OSD]]
- [[CSI]]
- [[StorageClass]]

# Ceph

`Ceph` — distributed storage system.

Ceph может давать:

```text
RBD block storage
CephFS filesystem
RGW S3-compatible object storage
```

В Kubernetes часто используется через [[Rook-Ceph]] и [[CSI]].

---

# Основные компоненты

```text
MON   monitors, cluster map/quorum
MGR   manager modules/metrics/dashboard
OSD   хранит данные на дисках
MDS   metadata server для CephFS
RGW   S3-compatible gateway
```

Смотри [[Ceph OSD]], [[Ceph RGW]].

---

# Health

```bash
ceph status
ceph health detail
ceph osd tree
ceph df
```

В Rook:

```bash
kubectl -n rook-ceph exec deploy/rook-ceph-tools -- ceph status
```

---

# Что важно

```text
replication/erasure coding
failure domains
OSD fullness
recovery/backfill impact
network latency
disk latency
monitor quorum
```

---

# Частые проблемы

## HEALTH_WARN full/nearfull

Ceph не любит заполненные диски. Нужен capacity planning.

## Slow ops

Проверять OSD latency, network, recovery, disks.

## Потеря failure domain

Если CRUSH map настроен плохо, replicas могут оказаться на одном host.

---

# Связанные заметки

- [[Rook-Ceph]]
- [[Ceph OSD]]
- [[Ceph RGW]]
- [[S3 Object Storage]]
- [[StorageClass]]

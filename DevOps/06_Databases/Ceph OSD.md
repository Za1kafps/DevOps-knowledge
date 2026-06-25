# Ceph OSD

`OSD` — Ceph daemon, который хранит данные на диске.

OSD отвечает за storage, replication/recovery и участие в CRUSH placement.

---

# Проверка

```bash
ceph osd tree
ceph osd status
ceph osd df
ceph health detail
```

В Rook:

```bash
kubectl -n rook-ceph get pods -l app=rook-ceph-osd
```

---

# Частые проблемы

```text
OSD down
disk full/nearfull
slow ops
backfill/recovery грузит cluster
один failure domain
```

---

# Связанные заметки

- [[Ceph]]
- [[Rook-Ceph]]
- [[Capacity Planning]]

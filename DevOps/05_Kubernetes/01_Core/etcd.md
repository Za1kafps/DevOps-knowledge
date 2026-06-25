# etcd

`etcd` — распределённое key-value хранилище, где Kubernetes хранит состояние cluster.

Если etcd потерян без backup, control plane теряет память о ресурсах.

---

# Что хранится в etcd

```text
Pods metadata
Deployments
Services
Secrets
ConfigMaps
CRDs
RBAC
events metadata
leases
```

Secrets в etcd могут быть зашифрованы encryption at rest, если это настроено. По умолчанию Kubernetes Secret — это не “магически безопасный vault”.

---

# Почему etcd критичен

API Server читает и пишет состояние в etcd.

Запущенные Pods могут продолжать работать при проблемах control plane, но:

```text
нельзя нормально создавать/изменять ресурсы
controllers не смогут reconciliate
scheduler не сможет планировать новые Pods
```

---

# Backup

Для kubeadm/control plane:

```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

Проверить snapshot:

```bash
ETCDCTL_API=3 etcdctl snapshot status snapshot.db -w table
```

Backup без restore drill — это надежда, а не backup.

---

# Health

```bash
ETCDCTL_API=3 etcdctl endpoint health -w table
ETCDCTL_API=3 etcdctl endpoint status -w table
```

Смотреть:

```text
leader
raft term
db size
latency
alarms
```

---

# Частые проблемы

## Большая latency диска

etcd чувствителен к fsync latency. Медленный диск ломает API responsiveness.

## Нет quorum

Для HA etcd нужен quorum. В кластере из 3 members можно потерять 1.

## DB разрослась

Нужны compaction/defrag по правилам конкретного deployment.

---

# Связанные заметки

- [[Kubernetes Architecture]]
- [[API Server]]
- [[Disaster Recovery]]
- [[Backup Strategy]]

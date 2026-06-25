# Calico

`Calico` — Kubernetes CNI для Pod networking и NetworkPolicy.

Calico может работать через routed networking или overlay, в зависимости от установки.

---

# Что даёт

```text
Pod networking
NetworkPolicy enforcement
BGP routing options
IPAM
egress controls в расширенных вариантах
```

---

# Проверка

```bash
kubectl -n kube-system get pods -l k8s-app=calico-node -o wide
kubectl -n kube-system logs ds/calico-node
```

Если установлен `calicoctl`:

```bash
calicoctl node status
calicoctl get ippool -o wide
```

---

# Частые проблемы

```text
BGP session down
IP pool пересекается с другой сетью
NetworkPolicy selector неверный
MTU при overlay
node firewall режет overlay/BGP traffic
```

---

# Связанные заметки

- [[CNI]]
- [[NetworkPolicy]]
- [[IPAM]]
- [[Pod-to-Pod Networking]]

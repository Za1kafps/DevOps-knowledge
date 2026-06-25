# IPAM

`IPAM` — IP Address Management.

В Kubernetes IPAM отвечает за выдачу Pod IP из Pod CIDR.

---

# Что важно

```text
Pod CIDR не пересекается с node/VPN/VPC networks
на каждую node хватает Pod IP
service CIDR не пересекается с Pod CIDR
CNI корректно освобождает IP после удаления Pod
```

---

# Симптомы проблем

```text
Pods не создаются
CNI failed to assign IP
закончились IP на node
traffic идёт не туда из-за overlapping CIDR
```

---

# Проверка

```bash
kubectl get nodes -o yaml | grep -i podCIDR -A2
kubectl get pods -A -o wide
kubectl -n kube-system logs ds/calico-node
kubectl -n kube-system logs ds/cilium
```

Команды зависят от CNI.

---

# Связанные заметки

- [[CNI]]
- [[Subnetting and CIDR]]
- [[Kubernetes Networking]]
- [[VPN]]

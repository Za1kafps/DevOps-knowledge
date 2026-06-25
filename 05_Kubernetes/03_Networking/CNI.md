# CNI

`CNI` — Container Network Interface.

В Kubernetes CNI plugin отвечает за Pod networking: выдаёт Pod IP, настраивает маршруты/interfaces и обеспечивает связь Pod-to-Pod.

---

# Что должен обеспечить CNI

Kubernetes networking model ожидает:

```text
Pod может общаться с Pod без NAT
node может общаться с Pod
Pod IP уникален в cluster
Service routing работает поверх Pod endpoints
```

Как именно это реализовано, зависит от CNI.

---

# Популярные CNI

- [[Cilium]]
- [[Calico]]
- [[Flannel]]

Различия:

```text
overlay или native routing
NetworkPolicy support
eBPF dataplane
encryption
observability
IPAM model
```

---

# CNI и NetworkPolicy

Kubernetes API имеет [[NetworkPolicy]], но enforcement делает CNI.

Если CNI не поддерживает NetworkPolicy, YAML применится, но traffic не будет фильтроваться.

---

# Диагностика

```bash
kubectl -n kube-system get pods -o wide
kubectl get nodes -o wide
kubectl get pods -A -o wide
```

Проверить Pod-to-Pod:

```bash
kubectl run tmp --rm -it --image=curlimages/curl -- sh
curl -v http://pod-ip:port
```

Смотреть logs конкретного CNI:

```bash
kubectl -n kube-system logs ds/cilium
kubectl -n kube-system logs ds/calico-node
```

---

# Частые проблемы

## Pods не получают IP

IPAM закончился или CNI daemon не работает.

## Pod-to-Pod не работает между nodes

Проблемы routes, encapsulation, MTU, firewall.

## NetworkPolicy не действует

CNI не поддерживает policy или policy selector неверный.

---

# Связанные заметки

- [[Kubernetes Networking]]
- [[Pod-to-Pod Networking]]
- [[NetworkPolicy]]
- [[IPAM]]
- [[MTU]]
- [[eBPF]]

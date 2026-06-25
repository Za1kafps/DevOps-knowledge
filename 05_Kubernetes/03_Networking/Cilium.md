# Cilium

`Cilium` — Kubernetes CNI на базе eBPF.

Он может выполнять Pod networking, NetworkPolicy, observability и service load balancing через eBPF dataplane.

---

# Что даёт

```text
Pod networking
Kubernetes NetworkPolicy
CiliumNetworkPolicy
eBPF service dataplane
Hubble observability
L7 policy в некоторых сценариях
```

---

# Проверка

```bash
kubectl -n kube-system get pods -l k8s-app=cilium -o wide
kubectl -n kube-system logs ds/cilium
cilium status
cilium connectivity test
```

Hubble:

```bash
hubble status
hubble observe
```

---

# Частые проблемы

```text
kernel/eBPF capabilities
Cilium agent not ready
policy drop
MTU/tunnel mode
kube-proxy replacement настройки
```

---

# Связанные заметки

- [[CNI]]
- [[eBPF]]
- [[NetworkPolicy]]
- [[Kubernetes Networking]]

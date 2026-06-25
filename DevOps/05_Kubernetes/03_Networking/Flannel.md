# Flannel

`Flannel` — простой Kubernetes CNI для Pod networking.

Часто используется как базовый overlay network, например VXLAN.

---

# Что важно

Flannel обычно решает Pod-to-Pod connectivity, но не является полноценным NetworkPolicy engine.

Если нужны NetworkPolicy, часто выбирают Calico/Cilium или отдельную связку.

---

# Проверка

```bash
kubectl -n kube-system get pods -l app=flannel -o wide
kubectl -n kube-system logs ds/kube-flannel-ds
kubectl get pods -A -o wide
```

---

# Частые проблемы

```text
VXLAN port blocked
MTU mismatch
Pod CIDR mismatch
flannel daemon not ready
```

---

# Связанные заметки

- [[CNI]]
- [[Pod-to-Pod Networking]]
- [[MTU]]

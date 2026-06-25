# kubelet

`kubelet` — агент Kubernetes на каждой node.

Он получает PodSpec от API Server и обеспечивает запуск containers через container runtime.

---

# Что делает kubelet

```text
register node
watch assigned Pods
create containers through CRI
run probes
mount volumes
report Pod/Node status
apply resource limits via cgroups
```

---

# Проверка node

```bash
kubectl get nodes
kubectl describe node <node>
```

На node:

```bash
systemctl status kubelet
journalctl -u kubelet -f
crictl ps
crictl logs <container-id>
```

---

# Частые проблемы

## Node NotReady

Причины:

```text
kubelet down
container runtime down
CNI problem
disk pressure
memory pressure
network to API Server
certificate issue
```

## Probes убивают containers

kubelet исполняет liveness/readiness/startup probes.

## Image garbage collection

При disk pressure kubelet чистит images/containers.

---

# Связанные заметки

- [[Kubernetes Architecture]]
- [[Pod]]
- [[Kubernetes Probes]]
- [[ImagePullBackOff]]

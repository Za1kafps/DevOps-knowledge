# Kubernetes Architecture

Kubernetes architecture делится на control plane и worker nodes.

```text
control plane:
  API Server
  etcd
  scheduler
  controller-manager

worker node:
  kubelet
  container runtime
  kube-proxy / CNI dataplane
  pods
```

---

# API Server

[[API Server]] — входная точка Kubernetes API.

Через него проходят:

```text
kubectl
controllers
scheduler
kubelet status updates
admission webhooks
operators
```

Если API Server недоступен, уже запущенные Pods обычно продолжают работать, но управлять cluster нельзя.

---

# etcd

[[etcd]] хранит состояние Kubernetes.

Там лежит desired state и metadata ресурсов.

Production правило:

```text
нет backup etcd = нет нормального disaster recovery control plane
```

---

# Scheduler

Scheduler выбирает node для Pod.

Он учитывает:

```text
requests
node selectors
affinity/anti-affinity
taints/tolerations
topology spread
volume constraints
```

Если Pod `Pending`, один из первых шагов — смотреть scheduler events.

---

# Controllers

Controllers постоянно сравнивают desired и actual state.

Примеры:

```text
Deployment controller создаёт ReplicaSet
ReplicaSet controller поддерживает replicas
Job controller следит за completion
EndpointSlice controller обновляет endpoints
```

---

# Kubelet

[[kubelet]] работает на каждой node.

Он получает PodSpec от API Server и через CRI просит container runtime запустить containers.

Также kubelet отправляет статусы Pod/Node обратно в API Server.

---

# CNI и kube-proxy

[[CNI]] отвечает за Pod networking.

[[kube-proxy]] или eBPF dataplane реализует Service routing.

Без CNI Pod не получит нормальную сеть.

Без service dataplane Service traffic не попадёт в endpoints.

---

# Проверка cluster

```bash
kubectl get componentstatuses
kubectl get --raw='/readyz?verbose'
kubectl get nodes -o wide
kubectl -n kube-system get pods -o wide
```

`componentstatuses` в новых версиях не всегда лучший источник правды; чаще полезнее `/readyz`, events и логи control plane.

---

# Связанные заметки

- [[API Server]]
- [[etcd]]
- [[kubelet]]
- [[kube-proxy]]
- [[CNI]]
- [[Kubernetes Events]]

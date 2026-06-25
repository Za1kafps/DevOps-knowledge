# Kubernetes

[[Kubernetes]] — система оркестрации контейнеров.

Она не “запускает Docker”, а управляет desired state: какие workloads должны быть запущены, где, с какими ресурсами, сетью, storage, секретами и политиками.

Упрощённая цепочка:

```text
kubectl / controller / CI
  -> API Server
  -> etcd stores desired state
  -> scheduler chooses node
  -> kubelet starts Pod via container runtime
  -> controllers reconcile actual state
```

---

# Главные ветки

## Control plane

- [[Kubernetes Architecture]]
- [[API Server]]
- [[etcd]]
- [[kubelet]]
- [[kube-proxy]]
- [[Namespace]]
- [[Container Runtime and CRI]]

Control plane хранит состояние, принимает API-запросы и запускает controllers.

---

## Workloads

- [[Pod]]
- [[Deployment]]
- [[ReplicaSet]]
- [[StatefulSet]]
- [[DaemonSet]]
- [[Job and CronJob]]
- [[Horizontal Pod Autoscaler]]
- [[PodDisruptionBudget]]
- [[Containers in a Pod]]
- [[Deployment vs StatefulSet]]

Workloads описывают, какие процессы должны работать.

---

## Health and resources

- [[Kubernetes Probes]]
- [[Readiness Probe]]
- [[Liveness Probe]]
- [[Startup Probe]]
- [[Resources Requests and Limits]]

Без readiness, requests и limits cluster быстро превращается в лотерею.

---

## Networking

- [[Kubernetes Networking]]
- [[Pod-to-Pod Networking]]
- [[Kubernetes Service]]
- [[ClusterIP]]
- [[NodePort]]
- [[LoadBalancer Service]]
- [[Endpoints]]
- [[EndpointSlice]]
- [[Ingress]]
- [[Nginx Ingress]]
- [[Gateway API]]
- [[CoreDNS]]
- [[CNI]]
- [[NetworkPolicy]]
- [[IPAM]]

Kubernetes networking строится вокруг идеи: Pod получает IP, Service даёт стабильную точку доступа, Ingress/Gateway публикует HTTP наружу.

---

## Storage

- [[PVC]]
- [[PV]]
- [[StorageClass]]
- [[CSI]]

Storage в Kubernetes — это отдельный lifecycle от Pod. Pod можно пересоздать, данные должны жить дальше.

---

## Security

- [[RBAC]]
- [[ServiceAccount]]
- [[Secrets]]
- [[ImagePullSecrets]]
- [[Kubernetes Security]]

Security в Kubernetes начинается с API access и заканчивается runtime-политиками Pod.

---

# Базовая диагностика

Понять, что происходит:

```bash
kubectl get pods -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl get nodes -o wide
```

Описание ресурса:

```bash
kubectl describe pod <pod> -n <namespace>
kubectl describe deploy <deploy> -n <namespace>
```

Логи:

```bash
kubectl logs <pod> -n <namespace>
kubectl logs <pod> -c <container> -n <namespace>
kubectl logs deploy/<deploy> -n <namespace>
```

Rollout:

```bash
kubectl rollout status deploy/<deploy> -n <namespace>
kubectl rollout history deploy/<deploy> -n <namespace>
```

---

# Что важно в production

```text
requests/limits заданы осознанно
readiness/liveness/startup probes не конфликтуют
rollout strategy контролирует downtime
PDB защищает от добровольных eviction
RBAC выдаёт минимальные права
NetworkPolicy ограничивает лишний traffic
Secrets не хранятся plaintext в Git
storage backup/restore проверены
observability покрывает cluster и приложения
```

---

# Частые симптомы

- [[ImagePullBackOff]]
- [[Kubernetes CrashLoopBackOff]]
- [[Kubernetes Service No Endpoints]]
- [[Pod Pending]]
- [[PVC Pending]]
- [[OOMKilled]]
- [[Ingress 502]]
- [[Kubernetes Pod Statuses]]

---

# Связанные заметки

- [[Containers]]
- [[CI-CD]]
- [[GitOps]]
- [[Observability]]
- [[Security]]
- [[Reliability and High Availability]]

# Deploy to Kubernetes

`Deploy to Kubernetes` — доставка новой версии приложения в Kubernetes cluster.

Это может быть push-based:

```bash
kubectl apply
helm upgrade
```

или pull-based через [[GitOps]].

---

# Что деплоят

```text
Deployment
Service
Ingress/Gateway
ConfigMap
Secret
Job/CronJob
HPA
PDB
NetworkPolicy
```

---

# kubectl apply

```bash
kubectl apply -f manifests/
kubectl rollout status deploy/app -n production
```

Проверить:

```bash
kubectl get pods -n production
kubectl get events -n production --sort-by=.lastTimestamp
```

---

# Важные проверки

```text
image tag/digest correct
namespace correct
resources requests/limits
readiness/liveness probes
config/secrets exist
service endpoints exist
ingress routes traffic
```

---

# Частые проблемы

## apply successful, app not ready

`kubectl apply` только отправил manifests в API server.

Нужно ждать rollout.

## ImagePullBackOff

Registry auth, tag, network или image не существует.

## Service has no endpoints

Pods не Ready или selector не совпадает.

---

# Связанные заметки

- [[Kubernetes]]
- [[Deployment]]
- [[Readiness Probe]]
- [[ImagePullBackOff]]
- [[Kubernetes Service No Endpoints]]
- [[GitOps]]

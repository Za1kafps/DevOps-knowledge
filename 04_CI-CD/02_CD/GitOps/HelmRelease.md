# HelmRelease

`HelmRelease` — FluxCD custom resource, который описывает Helm release декларативно.

Вместо ручного:

```bash
helm upgrade --install app chart
```

Flux читает `HelmRelease` из Git и сам приводит release к нужному состоянию.

---

# Пример

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: app
  namespace: app
spec:
  interval: 5m
  chart:
    spec:
      chart: ./charts/app
      sourceRef:
        kind: GitRepository
        name: apps
        namespace: flux-system
  values:
    image:
      repository: registry.example.com/app
      tag: v1.2.3
```

---

# Команды

```bash
flux get helmreleases -A
kubectl describe helmrelease app -n app
flux reconcile helmrelease app -n app
```

Смотреть Helm:

```bash
helm list -n app
helm history app -n app
```

---

# Что важно

```text
sourceRef должен быть Ready
chart path/name должен существовать
values должны давать валидные manifests
namespace должен существовать или создаваться отдельно
health/readiness workloads влияет на status
```

---

# Частые проблемы

## install retries exhausted

Chart не устанавливается.

Смотреть events и rendered manifests.

## timeout

Kubernetes resources не стали Ready.

## valuesFrom secret/configmap missing

HelmRelease ссылается на несуществующий Secret/ConfigMap.

---

# Связанные заметки

- [[FluxCD]]
- [[Helm]]
- [[Helm Chart]]
- [[GitOps Drift]]

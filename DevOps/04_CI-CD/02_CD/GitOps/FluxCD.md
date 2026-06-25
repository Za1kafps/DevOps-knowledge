# FluxCD

`FluxCD` — GitOps toolkit для Kubernetes.

Flux работает как набор controllers, которые читают sources, собирают desired state и применяют его в cluster.

Flux относится к [[GitOps]] и [[Continuous Delivery]], а не к CI.

---

# Что делает Flux

Flux умеет:

```text
следить за Git repository
следить за Helm repository / OCI registry
применять Kustomize manifests
устанавливать Helm releases
отслеживать image tags
автоматически обновлять image tag в Git
показывать Ready/NotReady status
```

---

# Основные controllers

## source-controller

Загружает sources:

```text
GitRepository
HelmRepository
OCIRepository
Bucket
```

Смотри [[GitRepository]].

---

## kustomize-controller

Применяет [[Kustomization]].

Это не только raw kustomize, а Flux custom resource, который указывает path, interval, dependencies и prune behavior.

---

## helm-controller

Управляет [[HelmRelease]].

Берёт chart из source и делает install/upgrade/rollback через Helm logic.

---

## image automation controllers

Следят за registry tags и обновляют Git:

- [[ImageRepository]]
- [[ImagePolicy]]
- [[ImageUpdateAutomation]]

---

# Базовые команды

Проверить всё:

```bash
flux get all -A
```

Sources:

```bash
flux get sources git -A
flux get sources helm -A
```

Kustomizations:

```bash
flux get kustomizations -A
```

Helm releases:

```bash
flux get helmreleases -A
```

Логи:

```bash
flux logs -A --level=error
```

Принудительная reconcile:

```bash
flux reconcile source git apps -n flux-system
flux reconcile kustomization apps -n flux-system --with-source
```

---

# Как читать проблему

Flux почти всегда ломается слоями:

```text
source не скачался
manifest не собрался
apply failed
health check не прошёл
dependency не готова
image automation не нашла tag
push в Git запрещён
```

Начинать:

```bash
flux get all -A
kubectl describe kustomization <name> -n <ns>
kubectl describe helmrelease <name> -n <ns>
```

---

# Частые проблемы

## GitRepository not ready

Проверить:

```bash
flux get sources git -A
kubectl describe gitrepository repo -n flux-system
```

Причины:

```text
неверный URL
нет deploy key/token
branch/tag не существует
network/DNS до Git
```

---

## Kustomization path wrong

Flux скачал repo, но path не найден или kustomize build падает.

---

## HelmRelease timeout

Chart применился, но workload не стал Ready.

Смотреть:

```bash
kubectl get pods -n app
kubectl describe helmrelease app -n app
kubectl get events -n app --sort-by=.lastTimestamp
```

---

# Связанные заметки

- [[GitOps]]
- [[Continuous Delivery]]
- [[GitRepository]]
- [[Kustomization]]
- [[HelmRelease]]
- [[ImageRepository]]
- [[ImagePolicy]]
- [[ImageUpdateAutomation]]

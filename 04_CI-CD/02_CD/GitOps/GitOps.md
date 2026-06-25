# GitOps

`GitOps` — подход к [[Continuous Delivery]], где Git хранит desired state окружения, а controller приводит реальное состояние к этому описанию.

GitOps не заменяет CI.

Нормальная цепочка:

```text
developer push
  -> CI tests/build/scans
  -> CI push image to registry
  -> Git desired state updated
  -> GitOps controller reconciles cluster
```

То есть CI отвечает за качество artifact, GitOps — за доставку и reconciliation.

---

# Главная идея

Git становится source of truth:

```text
что лежит в Git, то должно быть в cluster
```

Controller постоянно сравнивает:

```text
desired state в Git
actual state в Kubernetes
```

Если есть отличие, controller пытается привести cluster к Git.

---

# Push CD vs GitOps

## Push-based CD

Pipeline сам применяет изменения:

```bash
kubectl apply -f manifests/
helm upgrade --install app chart/
```

Плюсы:

```text
просто
понятно
меньше компонентов
```

Минусы:

```text
CI имеет доступ к cluster
drift сложнее контролировать
desired state может жить только в логах pipeline
```

---

## Pull-based GitOps

Controller внутри cluster сам читает Git:

```text
FluxCD / Argo CD -> Git -> apply to cluster
```

Плюсы:

```text
Git audit trail
drift detection
меньше прямых production credentials в CI
удобно для Kubernetes
```

Минусы:

```text
нужна дисциплина repo structure
секреты надо решать отдельно
сложнее bootstrap
не всё удобно выражается декларативно
```

---

# Что является desired state

Обычно:

```text
Kubernetes manifests
HelmRelease
Kustomization
Helm values
image tag/digest
policies
namespaces
RBAC
```

Не надо хранить plaintext secrets.

Для secrets смотри:

- [[SOPS]]
- [[Sealed Secrets]]
- [[Secrets Management]]

---

# Основные инструменты

- [[FluxCD]]
- [[Argo CD]]
- [[Helm]]
- [[Kustomize]]
- [[SOPS]]
- [[Sealed Secrets]]

FluxCD часто удобен как toolkit из controllers.

Argo CD часто удобен UI, Application model и visibility для команд.

Оба решают GitOps/CD-задачу, но делают это разными UX и архитектурой.

---

# Где GitOps помогает

```text
много Kubernetes окружений
нужен audit через Git
важна drift correction
CI не должен иметь cluster-admin
нужно разделить build и deploy ownership
```

---

# Где GitOps может мешать

```text
маленький single-host проект
нет Kubernetes
команда не готова хранить manifests аккуратно
секреты и bootstrapping не продуманы
pipeline и controller одновременно владеют одним ресурсом
```

---

# Частые ошибки

## CI и GitOps борются за cluster

CI делает `kubectl apply`, Flux/Argo CD потом возвращает состояние из Git.

Нужно выбрать владельца ресурса.

---

## Image tag mutable

Если в Git стоит `latest`, controller не понимает, что реально изменилось.

Лучше:

```text
tag = git sha / semver
digest tracked
```

---

## Secrets лежат plaintext в Git

Так нельзя.

Нужны encrypted secrets или external secret manager.

---

# Связанные заметки

- [[CI-CD]]
- [[Continuous Delivery]]
- [[FluxCD]]
- [[Argo CD]]
- [[GitOps Repo Structure]]
- [[GitOps Drift]]
- [[ImageUpdateAutomation]]

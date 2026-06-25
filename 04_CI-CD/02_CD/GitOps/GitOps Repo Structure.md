# GitOps Repo Structure

GitOps repo хранит desired state окружений.

Хорошая структура должна отвечать:

```text
что относится к platform
что относится к applications
где dev/stage/prod
как переиспользуются base manifests
где secrets
кто владеет изменениями
```

---

# Простой вариант

```text
clusters/
  dev/
    apps/
    platform/
  stage/
    apps/
    platform/
  prod/
    apps/
    platform/
apps/
  backend/
    base/
    overlays/
      dev/
      stage/
      prod/
```

Это удобно с [[Kustomize]].

---

# Helm-вариант

```text
clusters/
  prod/
    apps/
      backend-helmrelease.yaml
helm-values/
  backend/
    values-dev.yaml
    values-stage.yaml
    values-prod.yaml
```

FluxCD обычно использует [[HelmRelease]], Argo CD может указывать chart и values в Application.

---

# Monorepo или отдельный repo

## App code и manifests вместе

Плюсы:

```text
разработчик видит всё рядом
изменение app и manifests можно review-ить вместе
```

Минусы:

```text
сложнее разделить access
GitOps controller читает app repo
много окружений могут шуметь в app repo
```

---

## Отдельный GitOps repo

Плюсы:

```text
чёткий ownership deploy state
проще RBAC
удобный audit environments
```

Минусы:

```text
нужна automation для обновления image tags
изменение кода и deploy state в разных PR
```

---

# Secrets

Нельзя хранить plaintext secrets.

Варианты:

```text
SOPS encrypted files
Sealed Secrets
External Secrets Operator
Vault integration
cloud secret manager
```

Смотри [[SOPS]] и [[Sealed Secrets]].

---

# Что не надо делать

```text
prod manifests лежат только в wiki
kubectl apply из laptop
latest в production manifests
один values.yaml на все окружения
plaintext secrets
автоматический commit в prod без review
```

---

# Связанные заметки

- [[GitOps]]
- [[FluxCD]]
- [[Argo CD]]
- [[Kustomize]]
- [[Helm]]
- [[SOPS]]

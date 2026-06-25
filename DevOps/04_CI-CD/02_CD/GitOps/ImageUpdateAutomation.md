# ImageUpdateAutomation

`ImageUpdateAutomation` — FluxCD resource, который обновляет image tag в Git по результату [[ImagePolicy]].

Это важный момент: Flux не просто “магически деплоит новый image”.

Он делает Git commit с новым tag, а потом обычный GitOps reconcile применяет desired state.

---

# Цепочка

```text
CI push image tag
ImageRepository scans registry
ImagePolicy chooses tag
ImageUpdateAutomation updates Git
Kustomization/HelmRelease applies new state
```

---

# Пример

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageUpdateAutomation
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 1m
  sourceRef:
    kind: GitRepository
    name: apps
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: flux@example.com
        name: flux
      messageTemplate: "Update image tags"
    push:
      branch: main
  update:
    path: ./clusters/prod
    strategy: Setters
```

---

# Команды

```bash
flux get image update -A
kubectl describe imageupdateautomation apps -n flux-system
flux reconcile image update apps -n flux-system
```

---

# Что важно

```text
у Flux должны быть права push в Git
update path должен совпадать с repo structure
branch protection может блокировать push
prod automation должна быть осознанной
```

Для production часто лучше делать PR-based promotion, а не прямой push в main.

---

# Частые проблемы

## Ничего не обновляется

Проверить всю цепочку:

```bash
flux get image all -A
```

## Push rejected

Branch protected, нет прав или требуется signed commit.

## Automation меняет не тот файл

Неверный path или markers/setters.

---

# Связанные заметки

- [[FluxCD]]
- [[ImageRepository]]
- [[ImagePolicy]]
- [[GitOps Repo Structure]]
- [[Continuous Delivery]]

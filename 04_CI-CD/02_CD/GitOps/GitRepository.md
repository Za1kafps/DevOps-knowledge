# GitRepository

`GitRepository` — FluxCD source resource, который описывает Git repository как источник desired state.

Он отвечает за скачивание Git repo в cluster и предоставление artifact другим controllers.

Связано с [[FluxCD]], [[Kustomization]], [[HelmRelease]].

---

# Пример

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 1m
  url: ssh://git@github.com/example/gitops.git
  ref:
    branch: main
  secretRef:
    name: apps-deploy-key
```

---

# Что важно

```text
url       откуда брать repo
ref       branch/tag/semver/commit
interval  как часто проверять
secretRef credentials для private repo
```

---

# Команды

```bash
flux get sources git -A
kubectl describe gitrepository apps -n flux-system
flux reconcile source git apps -n flux-system
```

---

# Частые проблемы

## Authentication failed

Неверный deploy key/token или нет доступа к repo.

## Branch not found

`spec.ref.branch` указывает на несуществующую branch.

## DNS/network до Git

Controller внутри cluster должен иметь доступ к Git provider.

---

# Связанные заметки

- [[FluxCD]]
- [[GitOps]]
- [[Kustomization]]
- [[ImageUpdateAutomation]]

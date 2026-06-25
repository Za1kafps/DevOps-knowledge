# Kustomization

`Kustomization` может означать две разные вещи.

Важно не путать:

```text
kustomize.config.k8s.io/kustomization.yaml  файл Kustomize
kustomize.toolkit.fluxcd.io/Kustomization   FluxCD custom resource
```

Эта заметка про FluxCD `Kustomization`.

---

# Что делает Flux Kustomization

Flux `Kustomization` указывает:

```text
из какого source брать manifests
какой path собрать
как часто reconciliate
нужно ли prune
какие health checks ждать
от каких Kustomization зависит
```

---

# Пример

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: apps
  path: ./clusters/prod/apps
  prune: true
  wait: true
  timeout: 3m
```

---

# Команды

```bash
flux get kustomizations -A
kubectl describe kustomization apps -n flux-system
flux reconcile kustomization apps -n flux-system --with-source
```

Логи:

```bash
flux logs -A --kind Kustomization --name apps
```

---

# Важные поля

## path

Путь внутри source repo.

Если path неверный, Flux не найдёт manifests.

## prune

Если `true`, Flux удаляет ресурсы, которые были убраны из Git.

Это полезно, но опасно при неправильном path.

## dependsOn

Позволяет задать порядок:

```text
namespaces -> CRDs -> operators -> apps
```

---

# Частые проблемы

## kustomize build failed

Ошибка в YAML, patch, missing resource.

## health check timeout

Ресурсы применились, но не стали Ready.

## prune удалил больше, чем ожидали

Проверь path и ownership ресурсов.

---

# Связанные заметки

- [[FluxCD]]
- [[GitRepository]]
- [[Kustomize]]
- [[GitOps Drift]]

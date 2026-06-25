# Kustomize

`Kustomize` — инструмент для сборки Kubernetes manifests без шаблонизатора.

Он берёт base manifests и накладывает patches/overlays.

Связано с [[GitOps]], [[Kustomization]], [[Kubernetes]].

---

# Идея base и overlays

```text
base/
  deployment.yaml
  service.yaml
overlays/
  dev/
    kustomization.yaml
  prod/
    kustomization.yaml
```

Base содержит общие manifests.

Overlay меняет environment-specific части:

```text
replicas
image tag
resources
ingress host
config
```

---

# Пример kustomization.yaml

```yaml
resources:
  - ../../base

patches:
  - path: deployment-patch.yaml

images:
  - name: registry.example.com/app
    newTag: v1.2.3
```

Собрать локально:

```bash
kustomize build overlays/prod
kubectl kustomize overlays/prod
```

Применить:

```bash
kubectl apply -k overlays/prod
```

---

# Kustomize vs Helm

Kustomize хорош, когда:

```text
уже есть plain Kubernetes YAML
нужно немного менять manifests по окружениям
не нужен сложный template logic
```

Helm хорош, когда:

```text
нужен package/chart
много параметров
есть external chart ecosystem
```

---

# Частые ошибки

## Patch не применяется

Resource name/apiVersion/kind не совпадают.

## Overlay стал сложнее chart

Если patches слишком много и они плохо читаются, возможно нужен Helm или другой подход.

## Secret generator меняет hash

Это может перезапускать workloads. Иногда это нужно, иногда нет.

---

# Связанные заметки

- [[GitOps]]
- [[Kustomization]]
- [[Helm]]
- [[Deploy to Kubernetes]]

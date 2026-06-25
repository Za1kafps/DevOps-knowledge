# Deploy via Helm

`Deploy via Helm` — установка или обновление Kubernetes приложения через Helm chart.

Helm подходит, когда приложение описано chart-ом и параметры окружений задаются values.

---

# Команда deploy

```bash
helm upgrade --install app ./chart \
  -n production \
  --create-namespace \
  -f values-prod.yaml \
  --wait \
  --timeout 5m
```

`--wait` важен: Helm ждёт готовности ресурсов.

---

# Проверка до deploy

Render:

```bash
helm template app ./chart -f values-prod.yaml
```

Lint:

```bash
helm lint ./chart
```

Diff, если установлен plugin:

```bash
helm diff upgrade app ./chart -n production -f values-prod.yaml
```

---

# Rollback

```bash
helm history app -n production
helm rollback app 3 -n production
```

Если Helm управляется GitOps controller, rollback лучше делать через Git.

---

# Частые проблемы

## values не те

Итоговый YAML отличается от ожиданий.

## release stuck

Проверить:

```bash
helm status app -n production
kubectl get events -n production --sort-by=.lastTimestamp
```

## CRD upgrade

CRD требуют отдельной стратегии, не всегда стоит доверять это обычному chart upgrade.

---

# Связанные заметки

- [[Helm]]
- [[Helm Chart]]
- [[HelmRelease]]
- [[Deploy to Kubernetes]]
- [[Rollback]]

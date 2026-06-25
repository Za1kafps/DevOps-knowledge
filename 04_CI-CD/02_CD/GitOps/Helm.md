# Helm

`Helm` — package manager для Kubernetes.

Helm chart описывает набор Kubernetes manifests с шаблонами и values.

Helm используется как в обычном CD, так и в GitOps через [[HelmRelease]] или Argo CD Application.

---

# Основные понятия

```text
Chart     пакет manifests/templates
Values    параметры chart
Release   установленный экземпляр chart
Repository хранилище charts
```

---

# Команды

Добавить repo:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Установить или обновить:

```bash
helm upgrade --install app ./chart -n app --create-namespace -f values-prod.yaml
```

Список releases:

```bash
helm list -A
```

История:

```bash
helm history app -n app
```

Rollback:

```bash
helm rollback app 3 -n app
```

---

# Template debug

Посмотреть YAML до apply:

```bash
helm template app ./chart -f values-prod.yaml
```

Проверить chart:

```bash
helm lint ./chart
```

Dry run:

```bash
helm upgrade --install app ./chart -n app -f values-prod.yaml --dry-run
```

---

# Helm в GitOps

В FluxCD обычно создают [[HelmRelease]].

В Argo CD Application может ссылаться на Helm chart и values.

Главное правило:

```text
values для окружения должны быть в Git
ручной helm upgrade не должен конфликтовать с GitOps controller
```

---

# Частые проблемы

## Values не те

Проверить итоговый template:

```bash
helm template app chart/ -f values.yaml
```

## Release stuck

```bash
helm status app -n app
helm history app -n app
```

## CRD lifecycle

Helm не всегда хорошо управляет upgrade/delete CRD. С CRD нужна отдельная стратегия.

---

# Связанные заметки

- [[Helm Chart]]
- [[HelmRelease]]
- [[GitOps]]
- [[Deploy via Helm]]
- [[Rollback]]

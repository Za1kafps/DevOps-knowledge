# Helm Chart

`Helm Chart` — пакет Kubernetes manifests для [[Helm]].

Chart содержит templates, default values и metadata.

---

# Структура

```text
chart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
  charts/
```

`Chart.yaml` — metadata chart.

`values.yaml` — значения по умолчанию.

`templates/` — шаблоны Kubernetes manifests.

---

# Проверка chart

```bash
helm lint ./chart
helm template app ./chart -f values-prod.yaml
```

Установка:

```bash
helm upgrade --install app ./chart -n app -f values-prod.yaml
```

---

# Хороший chart

```text
не содержит secrets plaintext
имеет values schema если chart сложный
поддерживает resources/probes/securityContext
не генерирует случайные значения на каждый template
имеет понятные defaults
```

---

# Частые ошибки

## Слишком умные templates

Если template превращается в программирование на Go templates, chart становится трудно сопровождать.

## Разные окружения через копипасту chart

Лучше один chart и разные values.

## Secret в values.yaml

Values часто лежат в Git, поэтому secrets надо шифровать или брать извне.

---

# Связанные заметки

- [[Helm]]
- [[HelmRelease]]
- [[GitOps]]
- [[SOPS]]

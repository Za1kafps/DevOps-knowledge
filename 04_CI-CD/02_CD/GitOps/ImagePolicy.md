# ImagePolicy

`ImagePolicy` — FluxCD resource, который выбирает нужный image tag из tags, найденных [[ImageRepository]].

ImagePolicy не меняет manifests сама. Она только определяет “какой tag подходит”.

---

# Пример semver

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: app
  namespace: flux-system
spec:
  imageRepositoryRef:
    name: app
  policy:
    semver:
      range: '>=1.0.0 <2.0.0'
```

---

# Пример alphabetical

Подходит для tags с git sha или timestamp, если формат продуман.

```yaml
policy:
  alphabetical:
    order: asc
```

---

# Команды

```bash
flux get image policy -A
kubectl describe imagepolicy app -n flux-system
```

---

# Важные вопросы

```text
какой формат tags?
можно ли сортировать их как semver?
нужно ли исключить prerelease?
как policy отличает dev от prod?
```

Если tags хаотичные, image automation будет выбирать неожиданно.

---

# Частые проблемы

## Выбран не тот tag

Причина почти всегда в policy или формате tags.

## Semver не видит tag

Tag должен быть совместим с semver.

## Prod подтянул dev image

Нужны отдельные repositories, tag prefixes или строгие policies.

---

# Связанные заметки

- [[FluxCD]]
- [[ImageRepository]]
- [[ImageUpdateAutomation]]
- [[Container Registry]]

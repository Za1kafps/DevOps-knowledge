# ImageRepository

`ImageRepository` — FluxCD resource, который сканирует container registry и получает список tags.

Он не деплоит image сам.

Он даёт данные для [[ImagePolicy]].

---

# Пример

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: app
  namespace: flux-system
spec:
  image: registry.example.com/team/app
  interval: 1m
  secretRef:
    name: registry-auth
```

---

# Команды

```bash
flux get image repository -A
kubectl describe imagerepository app -n flux-system
```

Все image automation resources:

```bash
flux get image all -A
```

---

# Частые проблемы

## access denied

Нет credentials к registry.

## no tags found

Неверный image path или registry не отдаёт tags.

## rate limit

Registry ограничивает частые запросы.

Увеличь interval или настрой auth.

---

# Связанные заметки

- [[FluxCD]]
- [[ImagePolicy]]
- [[ImageUpdateAutomation]]
- [[Container Registry]]

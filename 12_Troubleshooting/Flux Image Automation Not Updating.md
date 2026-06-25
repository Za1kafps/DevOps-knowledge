# Flux Image Automation Not Updating

Flux image automation не обновляет Git/image tag.

---

# Проверка цепочки

```bash
flux get image all -A
kubectl describe imagerepository <name> -n flux-system
kubectl describe imagepolicy <name> -n flux-system
kubectl describe imageupdateautomation <name> -n flux-system
```

---

# Частые причины

```text
ImageRepository не видит registry
нет credentials
ImagePolicy не выбирает tag
tag format не semver
ImageUpdateAutomation не имеет push rights
branch protected
wrong update path/markers
```

---

# Связанные заметки

- [[ImageRepository]]
- [[ImagePolicy]]
- [[ImageUpdateAutomation]]
- [[Container Registry]]

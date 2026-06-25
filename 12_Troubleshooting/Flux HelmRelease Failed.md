# Flux HelmRelease Failed

Flux HelmRelease Failed — helm-controller не смог установить или обновить release.

---

# Проверка

```bash
flux get helmreleases -A
kubectl describe helmrelease <name> -n <ns>
flux logs -A --kind HelmRelease --name <name>
helm history <release> -n <ns>
```

---

# Частые причины

```text
sourceRef not ready
chart not found
values invalid
rendered manifest invalid
timeout waiting resources
missing valuesFrom Secret/ConfigMap
CRD issue
```

---

# Связанные заметки

- [[FluxCD]]
- [[HelmRelease]]
- [[Helm]]
- [[Kubernetes Events]]

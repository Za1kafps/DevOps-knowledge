# EndpointSlice

`EndpointSlice` хранит endpoints для Kubernetes Service более масштабируемо, чем старый Endpoints object.

Service traffic фактически идёт к адресам из EndpointSlices.

---

# Проверка

```bash
kubectl get endpointslice -A
kubectl get endpointslice -n app -l kubernetes.io/service-name=backend
kubectl describe endpointslice <slice> -n app
```

---

# Что смотреть

```text
addresses
ports
conditions.ready
targetRef
nodeName
zone
```

Если `ready=false`, Service не должен отправлять обычный traffic в endpoint.

---

# Частые проблемы

```text
нет slices для Service
Pod labels не совпали с selector
readiness failed
port name/number mismatch
```

---

# Связанные заметки

- [[Kubernetes Service]]
- [[Endpoints]]
- [[Readiness Probe]]

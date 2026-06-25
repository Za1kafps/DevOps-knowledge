# Endpoints

`Endpoints` — список backend IP:port для Service.

В новых Kubernetes чаще используется [[EndpointSlice]], но смысл тот же: Service должен знать, куда отправлять traffic.

---

# Проверка

```bash
kubectl get endpoints -n app
kubectl describe endpoints backend -n app
kubectl get endpointslice -n app
```

Если endpoints пустые, Service не имеет ready backend.

---

# Почему endpoints пустые

```text
selector Service не совпадает с labels Pods
Pods не Ready
Pods в другом namespace
targetPort mismatch
controller ещё не обновил slices
```

---

# Связанные заметки

- [[Kubernetes Service]]
- [[EndpointSlice]]
- [[Readiness Probe]]
- [[Kubernetes Service No Endpoints]]

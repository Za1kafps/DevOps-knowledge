# Kubernetes Service No Endpoints

`Service No Endpoints` означает: Service есть, но у него нет ready backend Pods.

---

# Проверка

```bash
kubectl get svc -n app
kubectl get endpoints -n app
kubectl get endpointslice -n app
kubectl describe svc backend -n app
kubectl get pods -n app --show-labels
```

---

# Частые причины

```text
selector Service не совпадает с labels Pods
Pods не Ready
Pods в другом namespace
targetPort wrong
Deployment не создал Pods
```

---

# Быстрый путь

1. Посмотреть selector:

```bash
kubectl get svc backend -n app -o yaml
```

2. Сравнить labels:

```bash
kubectl get pods -n app --show-labels
```

3. Проверить readiness:

```bash
kubectl describe pod pod-name -n app
```

---

# Связанные заметки

- [[Kubernetes Service]]
- [[Endpoints]]
- [[EndpointSlice]]
- [[Readiness Probe]]

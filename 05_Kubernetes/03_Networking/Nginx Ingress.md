# Nginx Ingress

`Nginx Ingress` — Ingress Controller на базе Nginx.

Он читает Ingress resources и генерирует Nginx config для маршрутизации HTTP/HTTPS traffic.

---

# Проверка

```bash
kubectl get ingress -A
kubectl get ingressclass
kubectl -n ingress-nginx get pods,svc
kubectl -n ingress-nginx logs deploy/ingress-nginx-controller
```

---

# Частые annotations

```text
nginx.ingress.kubernetes.io/proxy-read-timeout
nginx.ingress.kubernetes.io/proxy-body-size
nginx.ingress.kubernetes.io/rewrite-target
nginx.ingress.kubernetes.io/backend-protocol
```

Используй annotations осознанно: они завязаны на конкретный controller.

---

# Частые проблемы

```text
wrong ingressClass
default backend 404
Service endpoints empty
backend protocol HTTP/HTTPS mismatch
body too large 413
upstream timeout 504
```

---

# Связанные заметки

- [[Ingress]]
- [[Ingress Controller]]
- [[Nginx]]
- [[Ingress 502]]

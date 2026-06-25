# Ingress Controller

`Ingress Controller` — компонент, который реализует Kubernetes Ingress.

Ingress resource сам traffic не обрабатывает. Controller читает Ingress и настраивает proxy/load balancer.

---

# Примеры

```text
ingress-nginx
NGINX Ingress Controller
Traefik
HAProxy Ingress
cloud provider controllers
```

---

# Проверка

```bash
kubectl get ingressclass
kubectl get ingress -A
kubectl get pods -A | grep ingress
kubectl describe ingress <name> -n <ns>
```

---

# Частые проблемы

```text
ingressClassName не совпал
controller не смотрит namespace
LoadBalancer IP не выдан
TLS secret не найден
backend Service без endpoints
```

---

# Связанные заметки

- [[Ingress]]
- [[Nginx Ingress]]
- [[Gateway API]]

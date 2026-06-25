# Ingress

`Ingress` описывает HTTP/HTTPS routing к Kubernetes Services.

Ingress resource не принимает traffic сам. Нужен [[Ingress Controller]].

```text
client -> load balancer -> ingress controller -> Service -> Pod
```

---

# Пример

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app
spec:
  ingressClassName: nginx
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: app
                port:
                  number: 80
```

---

# Проверка

```bash
kubectl get ingress -A
kubectl describe ingress app -n app
kubectl get ingressclass
kubectl get svc,endpointslice -n app
```

Проверить routing:

```bash
curl -v -H "Host: app.example.com" http://<ingress-ip>/
```

---

# Частые проблемы

```text
wrong ingressClassName
Service has no endpoints
wrong service port
TLS secret missing
rewrite-target ломает path
backend protocol mismatch
```

---

# Связанные заметки

- [[Ingress Controller]]
- [[Nginx Ingress]]
- [[Gateway API]]
- [[Kubernetes Service]]
- [[Ingress 502]]

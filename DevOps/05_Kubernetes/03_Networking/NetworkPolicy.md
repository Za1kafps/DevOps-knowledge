# NetworkPolicy

`NetworkPolicy` ограничивает traffic между Pods/namespaces/IP blocks.

Важно: enforcement делает CNI. Если CNI не поддерживает NetworkPolicy, policy не будет реально работать.

---

# Default deny ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
    - Ingress
```

---

# Разрешить traffic к app

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

---

# Диагностика

```bash
kubectl get networkpolicy -A
kubectl describe networkpolicy <name> -n <ns>
kubectl get pods -n <ns> --show-labels
```

Проверять traffic из debug Pod.

---

# Частые ошибки

## Забыли DNS egress

Pod не может резолвить имена.

## Labels не совпадают

Policy применена не к тем Pods или не применена вообще.

## Нет default deny

Allow policy без изоляции может ничего не ограничить.

---

# Связанные заметки

- [[CNI]]
- [[Kubernetes Security]]
- [[CoreDNS]]
- [[Firewall]]

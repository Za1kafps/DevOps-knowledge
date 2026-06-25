# Gateway API

`Gateway API` — более современная модель Kubernetes traffic routing по сравнению с Ingress.

Она разделяет роли инфраструктурной команды и владельцев приложений.

---

# Основные ресурсы

```text
GatewayClass
Gateway
HTTPRoute
TCPRoute
TLSRoute
GRPCRoute
```

---

# Идея

```text
platform team создаёт Gateway
app team создаёт HTTPRoute
controller реализует routing
```

---

# Проверка

```bash
kubectl get gatewayclass
kubectl get gateway -A
kubectl get httproute -A
kubectl describe httproute <name> -n <ns>
```

---

# Когда полезен

```text
много teams
сложная маршрутизация
нужно лучшее разделение ownership
нужны richer routing primitives
```

---

# Связанные заметки

- [[Ingress]]
- [[Ingress Controller]]
- [[Kubernetes Service]]

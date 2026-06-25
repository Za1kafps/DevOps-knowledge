# Deployment

`Deployment` управляет rollout stateless приложения.

Deployment создаёт [[ReplicaSet]], ReplicaSet поддерживает нужное количество [[Pod]].

```text
Deployment -> ReplicaSet -> Pods
```

---

# Когда использовать

Deployment подходит для:

```text
stateless web apps
API services
workers without stable identity
frontend services
```

Для stateful приложений со стабильными именами и storage смотри [[StatefulSet]].

Подробное сравнение гарантий identity, rollout и PVC: [[Deployment vs StatefulSet]].

---

# Пример

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      containers:
        - name: app
          image: registry.example.com/app:v1.2.3
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              memory: 256Mi
```

---

# Rollout

Проверить:

```bash
kubectl rollout status deploy/app -n app
kubectl rollout history deploy/app -n app
```

Откат:

```bash
kubectl rollout undo deploy/app -n app
```

Пауза:

```bash
kubectl rollout pause deploy/app -n app
kubectl rollout resume deploy/app -n app
```

---

# Strategy

Rolling update:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

Если `maxUnavailable: 0`, Kubernetes не должен уменьшать доступные Pods ниже desired replicas во время rollout, но нужны ресурсы для extra Pod.

---

# Частые проблемы

## ProgressDeadlineExceeded

Новая ReplicaSet не стала Ready за deadline.

Смотреть:

```bash
kubectl describe deploy app -n app
kubectl get rs -n app
kubectl get pods -n app
```

---

## Selector mismatch

Deployment selector должен совпадать с labels Pod template. Selector immutable.

---

## Нет readinessProbe

Service может отправлять traffic в Pod до готовности приложения.

---

# Связанные заметки

- [[Pod]]
- [[ReplicaSet]]
- [[Rolling Update]]
- [[Readiness Probe]]
- [[Resources Requests and Limits]]
- [[Rollback]]
- [[Deployment vs StatefulSet]]

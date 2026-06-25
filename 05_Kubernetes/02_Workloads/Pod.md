# Pod

`Pod` — минимальная единица запуска в Kubernetes.

Pod содержит один или несколько containers, которые разделяют:

```text
network namespace
IP address
volumes
часть lifecycle
```

Обычно напрямую Pods не создают. Их создают controllers: [[Deployment]], [[StatefulSet]], [[DaemonSet]], [[Job and CronJob]].

---

# Pod lifecycle

Основные фазы:

```text
Pending
Running
Succeeded
Failed
Unknown
```

Container внутри Pod может быть:

```text
Waiting
Running
Terminated
```

---

# Проверка

```bash
kubectl get pods -n app -o wide
kubectl describe pod pod-name -n app
kubectl logs pod-name -n app
kubectl logs pod-name -c container-name -n app
```

Смотреть events:

```bash
kubectl get events -n app --sort-by=.lastTimestamp
```

---

# Почему Pod может не стартовать

```text
image не скачался
нет resources на node
PVC не bound
Secret/ConfigMap не найден
init container падает
readiness/liveness probe ошибочна
securityContext запрещён policy
```

---

# Restart policy

Для обычных workloads:

```text
Always
```

Для Jobs:

```text
OnFailure
Never
```

Deployment ожидает долгоживущие Pods, Job ожидает завершение.

---

# Multi-container Pod

Несколько containers в Pod оправданы, если они должны жить рядом:

```text
sidecar proxy
log shipper
init helper
service mesh sidecar
```

Не надо складывать в один Pod независимые сервисы только “чтобы было удобно”.

Подробно про application, init, native sidecar, ephemeral и pause/infra containers:

- [[Containers in a Pod]]
- [[Container Runtime and CRI]]

---

# Связанные заметки

- [[Deployment]]
- [[StatefulSet]]
- [[Kubernetes Probes]]
- [[Resources Requests and Limits]]
- [[Kubernetes Pod Statuses]]

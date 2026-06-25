# OOMKilled

`OOMKilled` означает, что container/process был убит из-за превышения memory limit или memory pressure.

В Kubernetes обычно видно:

```text
Reason: OOMKilled
Exit Code: 137
```

---

# Проверка

```bash
kubectl describe pod pod-name -n app
kubectl logs pod-name -n app --previous
kubectl top pod pod-name -n app
```

Exit code:

```bash
kubectl get pod pod-name -n app -o jsonpath='{.status.containerStatuses[*].lastState.terminated.exitCode}'
```

---

# Причины

```text
memory leak
limit слишком низкий
startup peak
большой cache
запрос обрабатывает слишком много данных
нет streaming/batching
слишком много workers
```

---

# Что смотреть

```text
memory usage график
limit/request
время OOM относительно deploy
изменения traffic
размер payload/job
GC metrics
```

---

# Исправления

```text
увеличить memory limit как временная мера
найти leak
ограничить concurrency
streaming вместо загрузки в память
уменьшить cache
поставить requests/limits осознанно
```

---

# Связанные заметки

- [[Resources Requests and Limits]]
- [[Kubernetes CrashLoopBackOff]]
- [[Memory and OOM]]
- [[Capacity Planning]]

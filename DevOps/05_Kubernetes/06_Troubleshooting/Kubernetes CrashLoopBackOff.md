# Kubernetes CrashLoopBackOff

`CrashLoopBackOff` означает: container стартует, падает, Kubernetes ждёт и пробует снова.

Это уже ошибка runtime приложения или его окружения, а не image pull.

---

# Быстрая диагностика

```bash
kubectl get pod pod-name -n app
kubectl describe pod pod-name -n app
kubectl logs pod-name -n app --previous
kubectl get events -n app --sort-by=.lastTimestamp
```

`--previous` важен: текущий container мог уже перезапуститься, и обычные logs покажут пусто.

---

# Смотреть exit code

```bash
kubectl get pod pod-name -n app -o jsonpath='{.status.containerStatuses[*].lastState.terminated.exitCode}'
```

Часто:

```text
1    приложение завершилось с ошибкой
137  SIGKILL, часто OOMKilled
143  SIGTERM
```

---

# Частые причины

```text
неверная команда/entrypoint
нет env/config/secret
не может подключиться к DB
миграция падает на старте
permission denied
OOMKilled
liveness probe убивает приложение
```

---

# Если виновата liveness

Проверить events:

```text
Liveness probe failed
Back-off restarting failed container
```

Слишком агрессивная liveness probe может сама создать CrashLoop.

---

# Связанные заметки

- [[Pod]]
- [[Kubernetes Probes]]
- [[Liveness Probe]]
- [[OOMKilled]]
- [[Secrets]]
- [[Kubernetes Events]]

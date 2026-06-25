# Kubernetes Pod Statuses

Pod status помогает быстро выбрать направление диагностики.

---

# Частые статусы

```text
Pending             Pod не запланирован/не стартовал
Running             Pod запущен
CrashLoopBackOff    container падает циклом
ImagePullBackOff    image не скачивается
ErrImagePull        первичная ошибка pull
Completed           Job завершился
OOMKilled           container убит memory limit
ContainerCreating   создаются container/volumes/network
```

---

# Команды

```bash
kubectl get pods -A
kubectl describe pod <pod> -n <ns>
kubectl get events -n <ns> --sort-by=.lastTimestamp
kubectl logs <pod> -n <ns> --previous
```

---

# Связанные заметки

- [[Pod Pending]]
- [[ImagePullBackOff]]
- [[Kubernetes CrashLoopBackOff]]
- [[OOMKilled]]

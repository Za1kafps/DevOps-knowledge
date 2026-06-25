# Job and CronJob

`Job` запускает задачу до успешного завершения.

`CronJob` создаёт Jobs по расписанию.

---

# Job

Используется для:

```text
migrations
batch processing
one-time scripts
backup tasks
data imports
```

Проверка:

```bash
kubectl get jobs -A
kubectl describe job <job> -n <ns>
kubectl logs job/<job> -n <ns>
```

---

# CronJob

```yaml
schedule: "*/5 * * * *"
```

Проверка:

```bash
kubectl get cronjobs -A
kubectl describe cronjob <name> -n <ns>
```

---

# Важные поля

```text
backoffLimit
activeDeadlineSeconds
ttlSecondsAfterFinished
concurrencyPolicy
startingDeadlineSeconds
```

`concurrencyPolicy: Forbid` полезен, если предыдущий запуск ещё не завершился.

---

# Частые ошибки

## CronJob запускается параллельно

Нет `concurrencyPolicy`.

## Job висит бесконечно

Нет `activeDeadlineSeconds`.

## Логи пропали

Pod удалён cleanup-ом до расследования.

---

# Связанные заметки

- [[Database Migrations]]
- [[Backups]]
- [[Graceful Shutdown]]

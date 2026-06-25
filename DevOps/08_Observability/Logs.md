# Logs

`Logs` — события, которые приложение или система записывает во время работы.

Логи отвечают на вопрос:

```text
что произошло в конкретный момент?
```

---

# Что писать в logs

```text
timestamp
level
service
request_id / trace_id
message
error details
important dimensions: user/tenant only если безопасно
```

Не писать:

```text
passwords
tokens
private keys
PII без необходимости
```

---

# Levels

```text
debug  подробности для разработки
info   нормальные важные события
warn   странно, но сервис работает
error  операция не выполнена
fatal  процесс не может продолжать
```

Если всё `error`, alerts станут шумом.

---

# Kubernetes

```bash
kubectl logs pod-name -n app
kubectl logs deploy/app -n app
kubectl logs pod-name -c container -n app --previous
```

`--previous` нужен после restart.

---

# Structured logs

JSON logs проще парсить:

```json
{"level":"error","service":"api","trace_id":"abc","msg":"db timeout"}
```

---

# Связанные заметки

- [[Loki]]
- [[Tracing]]
- [[Incident Response Flow]]
- [[Audit Logs]]

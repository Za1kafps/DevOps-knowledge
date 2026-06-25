# Preview Environments

`Preview Environment` — временное окружение для конкретной branch или merge request.

Оно помогает проверить изменение до merge:

```text
frontend preview
API preview
full-stack review app
temporary namespace in Kubernetes
```

---

# Как работает

```text
MR opened
CI builds image
CD creates namespace/environment
app deployed with unique URL
tests/review
MR closed/merged
environment destroyed
```

---

# Что нужно

```text
unique name
isolated namespace/resources
temporary DNS/URL
separate secrets or safe test secrets
automatic cleanup
resource quotas
```

---

# Kubernetes пример идеи

```text
namespace: review-123
host: pr-123.example.com
image: app:mr-123-sha
```

Проверка:

```bash
kubectl get ns | grep review
kubectl get all -n review-123
```

---

# Частые проблемы

## Preview environments не удаляются

Нужен cleanup job по close/merge и scheduled garbage collection.

## Используют production secrets

Preview окружения менее доверенные, secrets должны быть отдельные.

## Конфликтуют DNS/hostnames

Имя должно быть уникальным и валидным.

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Pipeline Rules]]
- [[Kubernetes]]
- [[Docker Compose]]
- [[DNS]]

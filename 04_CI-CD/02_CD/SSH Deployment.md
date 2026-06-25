# SSH Deployment

`SSH Deployment` — то же семейство практик, что [[Deploy via SSH]].

Эта заметка оставлена как отдельная точка входа для поиска по базе.

---

# Когда использовать

Подходит:

```text
один сервер
маленький проект
Docker Compose deploy
нет Kubernetes
нужен простой и понятный процесс
```

Не подходит:

```text
много серверов
сложный rollout
нужен autoscaling
нужен GitOps/drift control
```

---

# Минимальный безопасный набор

```text
отдельный deploy user
SSH key только для CI
protected variables
known_hosts проверяется
команды deploy идемпотентны
есть healthcheck
есть rollback
```

---

# Связанные заметки

- [[Deploy via SSH]]
- [[Deploy via Docker Compose]]
- [[SSH]]
- [[Linux Server Setup]]

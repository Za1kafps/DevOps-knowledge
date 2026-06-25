# Deploy via SSH

`Deploy via SSH` — push-based CD, где pipeline подключается к серверу и выполняет команды deploy.

Это простой вариант для VPS/single-host проектов.

---

# Типовая схема

```text
CI build image
CI push image to registry
deploy job ssh to server
server docker compose pull
server docker compose up -d
healthcheck
```

---

# Пример

```bash
ssh deploy@app.example.com '
  cd /opt/app &&
  docker compose pull &&
  docker compose up -d &&
  docker compose ps
'
```

Healthcheck:

```bash
curl -f https://app.example.com/health
```

---

# SSH key

В CI храни private key как protected secret.

На сервере:

```text
deploy user
ограниченные sudo права или без sudo
authorized_keys
минимальные permissions
```

Не деплой под root без необходимости.

---

# Риски

```text
CI имеет доступ к серверу
логи могут раскрыть secrets
ручные изменения на сервере создают drift
rollback надо писать отдельно
```

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Deploy via Docker Compose]]
- [[SSH]]
- [[Docker Compose]]
- [[Rollback]]

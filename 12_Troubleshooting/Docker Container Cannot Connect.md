# Docker Container Cannot Connect

Контейнер не может подключиться к другому сервису, host или интернету.

---

# Проверка

```bash
docker ps
docker inspect <container>
docker network ls
docker network inspect <network>
docker exec -it <container> sh
```

Внутри:

```bash
ip route
getent hosts service
nc -vz host port
curl -v http://host:port
```

---

# Частые причины

```text
контейнеры в разных networks
используется localhost вместо service name
порт не опубликован
app слушает 127.0.0.1
DNS внутри Docker
host firewall
```

---

# Связанные заметки

- [[Docker Network]]
- [[Docker Compose]]
- [[Network]]

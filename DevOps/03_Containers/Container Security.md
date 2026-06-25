# Container Security

`Container Security` — безопасность запуска контейнера.

Она отличается от [[Image Security]]: image security про то, что внутри image, container security про то, как контейнер запущен.

Главная мысль: контейнер — это процесс на host kernel. Если дать ему лишние права, изоляция становится слабой.

---

# Что ограничивает контейнер

Linux-механизмы:

```text
namespaces
cgroups
capabilities
seccomp
AppArmor / SELinux
read-only filesystem
user namespaces
```

Docker делает часть ограничений по умолчанию, но production всё равно надо настраивать явно.

---

# Не запускать root без причины

В Dockerfile:

```dockerfile
RUN adduser -D app
USER app
```

Проверить:

```bash
docker run --rm image id
```

Root внутри контейнера не равен полноценному root на host, но при уязвимости runtime/kernel/volume mount последствия хуже.

---

# Capabilities

Linux capabilities дробят root-привилегии.

Запуск с минимизацией:

```bash
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE app
```

`NET_BIND_SERVICE` нужен, чтобы bind-ить порты ниже 1024.

Не надо использовать:

```bash
--privileged
```

без очень сильной причины.

---

# Read-only root filesystem

```bash
docker run --read-only --tmpfs /tmp app
```

Так приложение не сможет писать в root filesystem.

Если ему нужны writable dirs, задавай их явно:

```bash
--tmpfs /tmp
-v appdata:/var/lib/app
```

---

# Secrets

Не передавать secrets через image.

Плохо:

```dockerfile
COPY .env /app/.env
```

Лучше:

```text
runtime env
secret manager
Docker secrets
Kubernetes Secrets
Vault
```

Проверять:

```bash
docker history --no-trunc image
docker inspect container
```

`docker inspect` может показывать env, поэтому env secrets тоже не идеальны.

---

# Resource limits

Без лимитов контейнер может съесть host.

Пример:

```bash
docker run -d \
  --memory 512m \
  --cpus 1 \
  app
```

Проверить:

```bash
docker stats
```

---

# Опасные mount

Очень опасно:

```bash
-v /:/host
-v /var/run/docker.sock:/var/run/docker.sock
--privileged
--pid host
--network host
```

Docker socket внутри контейнера почти равен root доступу к host, потому что через него можно запустить privileged контейнер.

---

# Практический baseline

```bash
docker run -d \
  --name app \
  --user 10001:10001 \
  --read-only \
  --tmpfs /tmp \
  --cap-drop ALL \
  --security-opt no-new-privileges:true \
  --memory 512m \
  --cpus 1 \
  app:1.0.0
```

Не всё подходит каждому приложению, но это хороший baseline для размышления.

---

# Связанные заметки

- [[Containers]]
- [[Image Security]]
- [[Dockerfile]]
- [[Secrets Management]]
- [[Kubernetes Security]]
- [[Supply Chain Security]]

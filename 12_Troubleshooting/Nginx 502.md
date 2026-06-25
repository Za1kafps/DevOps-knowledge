# Nginx 502

`502 Bad Gateway` в Nginx означает, что Nginx не получил нормальный ответ от upstream.

---

# Быстрая проверка

Проверить конфиг:

```bash
sudo nginx -t
```

Логи:

```bash
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log
```

Проверить upstream с сервера:

```bash
curl -v http://127.0.0.1:8080/health
ss -lntp | grep 8080
```

---

# Частые причины

```text
upstream port не слушается
wrong proxy_pass protocol
app упал
app слушает 127.0.0.1 в другом namespace/container
timeout
DNS upstream не резолвится
```

---

# Protocol mismatch

Nginx proxy_pass HTTP, а upstream ждёт HTTPS:

```nginx
proxy_pass http://backend;
```

При необходимости:

```nginx
proxy_pass https://backend;
```

---

# Связанные заметки

- [[Nginx]]
- [[Reverse Proxy]]
- [[Ingress 502]]
- [[Kubernetes Service No Endpoints]]

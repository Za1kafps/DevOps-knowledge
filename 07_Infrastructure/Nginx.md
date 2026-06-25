# Nginx

`Nginx` — web server и reverse proxy.

В DevOps чаще всего используется как:

```text
reverse proxy
TLS termination
static files server
load balancer
ingress controller dataplane
gateway перед app
```

---

# Базовая схема reverse proxy

```text
client -> Nginx :443
Nginx -> app :8080
```

Пример:

```nginx
server {
    listen 443 ssl http2;
    server_name app.example.com;

    ssl_certificate /etc/letsencrypt/live/app/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/app/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

# Команды

Проверить конфиг:

```bash
sudo nginx -t
```

Reload:

```bash
sudo systemctl reload nginx
```

Status:

```bash
systemctl status nginx
```

Logs:

```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

---

# Частые 502 причины

```text
upstream port не слушается
wrong proxy_pass protocol
app слушает 127.0.0.1/другой interface
connection refused
upstream timeout
DNS upstream не резолвится
```

Проверить с сервера:

```bash
curl -v http://127.0.0.1:8080/health
ss -lntp | grep 8080
```

---

# Timeouts

Важные настройки:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 60s;
proxy_read_timeout 60s;
client_max_body_size 20m;
```

`client_max_body_size` связан с HTTP 413.

---

# Связанные заметки

- [[Reverse Proxy]]
- [[TLS Certificates]]
- [[Nginx 502]]
- [[Load Balancing]]
- [[Ingress]]

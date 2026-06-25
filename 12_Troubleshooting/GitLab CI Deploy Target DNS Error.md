# GitLab CI Deploy Target DNS Error

GitLab CI deploy target DNS error — runner не может резолвить host deploy target.

---

# Проверка в job

```bash
cat /etc/resolv.conf
getent hosts deploy.example.com
nslookup deploy.example.com
dig deploy.example.com
```

---

# Частые причины

```text
неверный hostname variable
private DNS недоступен runner
VPN/network не подключен
split-horizon DNS
resolver в runner container
deploy target placeholder не заменён
```

---

# Что делать

```text
проверить CI variables
проверить runner network
использовать FQDN
не хардкодить временные placeholder hosts
```

---

# Связанные заметки

- [[GitLab CI]]
- [[DNS]]
- [[Deploy via SSH]]

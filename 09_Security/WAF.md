# WAF

`WAF` — Web Application Firewall.

Он фильтрует HTTP traffic до приложения.

---

# Что может ловить

```text
SQL injection patterns
XSS patterns
path traversal
bad bots
protocol anomalies
rate abuse
known CVE exploit patterns
```

---

# Где ставят

```text
CDN/edge
load balancer
Ingress
API gateway
reverse proxy
```

---

# Важно

WAF не заменяет secure coding.

Он снижает риск и даёт дополнительный слой защиты, но может давать false positives.

---

# Связанные заметки

- [[Cloudflare WAF]]
- [[Rate Limiting]]
- [[Security]]
- [[HTTP]]

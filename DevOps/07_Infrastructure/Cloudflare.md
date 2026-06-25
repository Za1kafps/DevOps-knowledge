# Cloudflare

`Cloudflare` — edge/CDN/DNS/WAF платформа.

В DevOps часто используется для:

```text
DNS
CDN cache
TLS edge termination
WAF
DDoS protection
Access/ZeroTrust
rate limiting
```

---

# Что проверять

```text
DNS records
proxy status orange/gray cloud
SSL/TLS mode
origin certificate
WAF events
cache rules
page/redirect rules
```

---

# Частые проблемы

```text
DNS proxied скрывает origin IP
SSL mode Flexible ломает HTTPS к origin
WAF false positive
cache отдаёт старый content
origin недоступен, edge показывает 52x
```

---

# Связанные заметки

- [[DNS]]
- [[Cloudflare WAF]]
- [[TLS Certificates]]
- [[ZeroTrust]]

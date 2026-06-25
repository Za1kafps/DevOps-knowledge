# Cloudflare WAF

`Cloudflare WAF` фильтрует HTTP traffic на edge Cloudflare.

---

# Что смотреть

```text
Security Events
rule id
action block/challenge/log
matched payload
source IP/country/ASN
URI/path
bot score
```

---

# Практика

Перед блокировкой новой rule лучше включить log/challenge mode и посмотреть false positives.

Для API важно не сломать legitimate clients.

---

# Частые проблемы

```text
false positive на API payload
заблокирован healthcheck
реальный client IP не доходит до origin
rate limit слишком грубый
```

---

# Связанные заметки

- [[WAF]]
- [[Cloudflare]]
- [[Rate Limiting]]
- [[HTTP]]

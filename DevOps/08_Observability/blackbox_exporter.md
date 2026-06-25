# blackbox_exporter

`blackbox_exporter` проверяет сервис снаружи как клиент.

Он нужен для synthetic monitoring:

```text
HTTP доступен?
TLS сертификат валиден?
DNS работает?
TCP port открыт?
ICMP ping проходит?
```

---

# Почему это важно

Внутренние метрики приложения могут быть зелёными, но пользователь не может открыть сайт из-за DNS/TLS/LB.

Blackbox проверяет путь ближе к user experience.

---

# HTTP probe

Prometheus scrape обычно идёт на blackbox exporter:

```text
/probe?target=https://example.com&module=http_2xx
```

Полезные метрики:

```promql
probe_success
probe_duration_seconds
probe_http_status_code
probe_ssl_earliest_cert_expiry
```

---

# TLS expiry

Alert:

```promql
(probe_ssl_earliest_cert_expiry - time()) / 86400 < 14
```

---

# Частые ошибки

## Проверка изнутри cluster

Она не доказывает, что сервис доступен пользователю из интернета.

## Один регион probes

Можно не увидеть regional routing problem.

## Нет Host/SNI

Для HTTPS virtual hosts важно проверять правильный domain.

---

# Связанные заметки

- [[Prometheus]]
- [[TLS certificate expired]]
- [[DNS Failure]]
- [[SLO]]

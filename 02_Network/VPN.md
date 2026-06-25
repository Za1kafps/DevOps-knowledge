# VPN

`VPN` — зашифрованный сетевой туннель между клиентом, сервером или сетями.

VPN используют, чтобы:

```text
дать доступ к private сетям
соединить офис и cloud
закрыть admin endpoints от интернета
маршрутизировать traffic через другой gateway
строить site-to-site connectivity
```

Связано с [[Routing]], [[Firewall]], [[NAT]], [[MTU]], [[UDP]].

---

# Виды VPN

## Remote access

Пользователь подключается к private сети.

Пример:

```text
laptop -> VPN server -> internal services
```

---

## Site-to-site

Соединяются две сети.

Пример:

```text
office 10.10.0.0/16 <-> cloud 10.20.0.0/16
```

Тут особенно важно, чтобы CIDR не пересекались.

---

# Популярные технологии

## WireGuard

Простой современный VPN, обычно работает по UDP.

Проверка:

```bash
sudo wg show
ip route
```

---

## OpenVPN

Гибкий VPN, может работать по UDP или TCP.

Проверка:

```bash
systemctl status openvpn
journalctl -u openvpn -f
```

---

## IPsec

Часто используется для site-to-site между cloud/on-prem routers.

Сложнее в настройке, но распространён в enterprise.

---

# Что VPN меняет в системе

После подключения обычно появляются:

```text
новый network interface
новые routes
новый DNS resolver
новые firewall правила
иногда default route через VPN
```

Проверять:

```bash
ip addr
ip route
resolvectl status
```

---

# Split tunnel и full tunnel

Split tunnel:

```text
только private сети идут в VPN
интернет идёт напрямую
```

Full tunnel:

```text
весь traffic идёт через VPN
```

Full tunnel проще контролировать, но он влияет на latency, bandwidth и доступность интернета у клиента.

---

# Диагностика

Проверить интерфейс:

```bash
ip -br addr
```

Проверить route до private IP:

```bash
ip route get 10.20.1.15
```

Проверить DNS:

```bash
dig internal.example.local
```

Проверить порт:

```bash
nc -vz 10.20.1.15 5432
```

Проверить пакеты:

```bash
sudo tcpdump -i any host 10.20.1.15
```

---

# Частые проблемы

## Пересекающиеся CIDR

Если локальная сеть пользователя `192.168.1.0/24` и удалённая сеть тоже `192.168.1.0/24`, routing становится неоднозначным.

---

## DNS работает только внутри VPN

После подключения должен примениться resolver для внутренних зон.

Проверить:

```bash
resolvectl status
cat /etc/resolv.conf
```

---

## MTU

VPN добавляет overhead.

Симптом:

```text
ssh работает
web pages зависают
docker pull ломается
```

Смотри [[MTU]].

---

# Связанные заметки

- [[Routing]]
- [[Firewall]]
- [[NAT]]
- [[MTU]]
- [[DNS]]
- [[Security]]

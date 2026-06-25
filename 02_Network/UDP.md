# UDP

`UDP` — транспортный протокол без соединения.

Он отправляет datagram и не делает handshake, retransmit, ordering и flow control.

UDP используют там, где важны низкая задержка, простота или где надёжность реализована выше:

```text
DNS
QUIC / HTTP/3
WireGuard
VoIP
streaming
service discovery
metrics shipping
```

---

# Чем UDP отличается от TCP

У [[TCP]] есть соединение:

```text
SYN -> SYN-ACK -> ACK -> data
```

У UDP:

```text
client -> datagram -> server
```

Если пакет потерялся, UDP сам его не повторит.

Если пакеты пришли не по порядку, UDP сам порядок не восстановит.

---

# Почему DNS часто UDP

Обычный DNS-запрос маленький, поэтому UDP подходит хорошо.

Проверить:

```bash
dig example.com
```

Принудительно TCP:

```bash
dig +tcp example.com
```

DNS может перейти на TCP для больших ответов, zone transfer и некоторых DNSSEC-сценариев.

---

# Проверка UDP

UDP сложнее проверять, чем TCP, потому что нет handshake.

Слушающие UDP-сокеты:

```bash
sudo ss -lunp
```

Проверить DNS:

```bash
dig @1.1.1.1 example.com
```

Проверить пакеты:

```bash
sudo tcpdump -i any -nn 'udp port 53'
```

Для произвольного UDP:

```bash
nc -u -vz host 51820
```

Важно: `nc -u` не всегда может надёжно сказать, открыт порт или нет.

---

# UDP и firewall

Для UDP отсутствие ответа не говорит точно, где проблема.

Возможные варианты:

```text
packet dropped firewall
service не слушает
service получил пакет, но не обязан отвечать
ответ ушёл другим route
```

Поэтому UDP почти всегда проверяют через `tcpdump` на обеих сторонах.

---

# MTU и UDP

UDP чувствителен к большим datagram.

Если пакет больше path MTU, он может фрагментироваться или потеряться.

Это особенно важно для:

```text
VPN
WireGuard
VXLAN
DNS с большими ответами
QUIC
```

Связано с [[MTU]].

---

# Частые проблемы

## Открыли TCP, забыли UDP

Типично для DNS и VPN.

Пример:

```text
53/tcp открыт
53/udp закрыт
```

DNS будет работать странно или не работать вовсе.

---

## Нет ответа, но порт не обязательно закрыт

UDP-сервис может не отвечать на неправильный payload.

Поэтому проверяй прикладным клиентом:

```bash
dig
wg show
openvpn logs
```

---

# Связанные заметки

- [[Network]]
- [[DNS]]
- [[Firewall]]
- [[VPN]]
- [[MTU]]
- [[tcpdump]]

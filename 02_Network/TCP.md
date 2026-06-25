# TCP

`TCP` — транспортный протокол с соединением, подтверждениями доставки и контролем порядка байтов.

Через TCP работают [[HTTP]], [[HTTPS and TLS]], SSH, PostgreSQL, Redis, Kafka clients и большинство API.

TCP не знает про URL, headers и status codes. Он передаёт поток байтов между IP:port и IP:port.

---

# Что гарантирует TCP

TCP даёт:

```text
соединение перед передачей данных
доставку с retransmit
порядок байтов
контроль перегрузки
flow control
закрытие соединения
```

TCP не гарантирует, что приложение правильно обработало запрос. Он гарантирует только транспорт.

---

# TCP handshake

Перед передачей данных клиент и сервер делают handshake:

```text
client -> SYN
server -> SYN-ACK
client -> ACK
```

Если в `tcpdump` видно только `SYN`, но нет `SYN-ACK`, значит ответ не возвращается.

Частые причины:

```text
порт закрыт firewall
service не слушает порт
route назад сломан
security group drop
load balancer не видит backend
```

---

# TCP states

Посмотреть состояния:

```bash
ss -ant
```

Важные состояния:

```text
LISTEN       процесс слушает порт
SYN-SENT     клиент отправил SYN
SYN-RECV     сервер получил SYN и отправил SYN-ACK
ESTAB        соединение установлено
FIN-WAIT     соединение закрывается
CLOSE-WAIT   remote закрыл, local process ещё не закрыл socket
TIME-WAIT    соединение закрыто, ядро временно держит запись
```

Много `CLOSE-WAIT` часто указывает на проблему в приложении: оно не закрывает сокеты.

Много `TIME-WAIT` само по себе не всегда ошибка, но может упереться в ephemeral ports.

---

# Проверка порта

Проверить, слушает ли порт:

```bash
sudo ss -lntp | grep ':443'
```

Проверить подключение:

```bash
nc -vz example.com 443
```

Проверить через curl:

```bash
curl -v https://example.com
```

---

# Таймауты

`Connection refused`:

```text
хост ответил RST
порт закрыт или сервис не слушает
```

`Connection timed out`:

```text
ответ не пришёл
часто firewall drop или route problem
```

`Connection reset by peer`:

```text
удалённая сторона принудительно закрыла соединение
часто приложение, proxy, LB или firewall
```

---

# Keepalive

TCP keepalive помогает обнаруживать мёртвые соединения.

Проверить настройки:

```bash
sysctl net.ipv4.tcp_keepalive_time
sysctl net.ipv4.tcp_keepalive_intvl
sysctl net.ipv4.tcp_keepalive_probes
```

Для production важнее часто не kernel keepalive, а timeouts на уровне приложения, reverse proxy и load balancer.

---

# Диагностика tcpdump

Поймать handshake:

```bash
sudo tcpdump -i any -nn 'tcp port 443'
```

Флаги:

```text
S   SYN
S.  SYN-ACK
.   ACK
F   FIN
R   RST
P   PSH
```

---

# Связанные заметки

- [[Network]]
- [[HTTP]]
- [[HTTPS and TLS]]
- [[Load Balancing]]
- [[Firewall]]
- [[tcpdump]]
- [[ss]]

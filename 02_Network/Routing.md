# Routing

`Routing` — выбор пути, по которому пакет уйдёт к destination IP.

Маршрутизация отвечает на вопрос:

```text
через какой интерфейс и gateway отправить пакет?
```

Связано с [[IPv4]], [[IPv6]], [[Subnetting and CIDR]], [[NAT]], [[VPN]] и [[Firewall]].

---

# Как Linux выбирает маршрут

У Linux есть таблица маршрутов.

Посмотреть:

```bash
ip route
```

Пример:

```text
default via 10.0.1.1 dev eth0
10.0.1.0/24 dev eth0 proto kernel scope link src 10.0.1.15
10.8.0.0/24 dev tun0
```

Смысл:

```text
10.0.1.0/24 доступна напрямую через eth0
10.8.0.0/24 доступна через VPN-интерфейс tun0
всё остальное идёт в default gateway 10.0.1.1
```

---

# Longest prefix match

Если подходит несколько маршрутов, выбирается самый специфичный.

Пример:

```text
10.0.1.0/24 -> через eth1
10.0.0.0/8  -> через eth0
```

Для `10.0.1.20` будет выбран `/24`, потому что он точнее.

---

# Проверить маршрут до IP

```bash
ip route get 8.8.8.8
```

Пример вывода:

```text
8.8.8.8 via 10.0.1.1 dev eth0 src 10.0.1.15
```

Это говорит:

```text
пакет уйдёт через eth0
gateway будет 10.0.1.1
source IP будет 10.0.1.15
```

---

# Default route

Default route используется, когда нет более точного маршрута.

Проверить:

```bash
ip route | grep default
```

Если default route отсутствует, сервер может видеть локальную сеть, но не иметь доступа в интернет.

---

# Traceroute

`traceroute` показывает промежуточные hop-ы до цели.

```bash
traceroute 8.8.8.8
tracepath example.com
```

Важно: отсутствие ответа от hop не всегда значит проблему. Многие маршрутизаторы режут ICMP TTL exceeded.

Для TCP-проверки:

```bash
traceroute -T -p 443 example.com
```

---

# Policy routing

Иногда одной таблицы маршрутов мало.

Например:

```text
трафик от одного source IP отправлять через один провайдер
трафик от другого source IP через другой
```

Проверить rules:

```bash
ip rule
ip route show table all
```

---

# Частые проблемы

## Нет default route

Симптом:

```text
локальные IP доступны, интернет нет
```

Проверить:

```bash
ip route
```

---

## Пакет уходит не в тот интерфейс

Часто бывает на серверах с несколькими интерфейсами, VPN или Docker/Kubernetes сетями.

Проверить:

```bash
ip route get <destination-ip>
```

---

## Ассиметричный routing

Запрос пришёл одним путём, ответ ушёл другим.

Симптомы:

```text
SYN приходит
SYN-ACK уходит не туда
connection timeout
firewall видит invalid state
```

Проверять через [[tcpdump]] на обоих интерфейсах.

---

# Связанные заметки

- [[Network]]
- [[Subnetting and CIDR]]
- [[NAT]]
- [[Firewall]]
- [[VPN]]
- [[tcpdump]]

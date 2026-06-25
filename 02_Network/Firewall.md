# Firewall

`Firewall` фильтрует сетевой трафик по правилам.

Он может разрешить, запретить или перенаправить пакеты по IP, порту, протоколу, интерфейсу и состоянию соединения.

Связано с [[Network]], [[TCP]], [[UDP]], [[Routing]], [[NAT]], [[VPN]].

---

# Что firewall проверяет

Обычно правило смотрит на:

```text
source IP
destination IP
source port
destination port
protocol: tcp/udp/icmp
interface
connection state
```

Пример:

```text
allow tcp from 10.0.0.0/8 to 10.0.1.10 port 5432
drop everything else
```

---

# Allow и drop

`allow` пропускает пакет.

`reject` отклоняет и часто отправляет ответ.

`drop` молча выбрасывает пакет.

Разница в симптомах:

```text
reject -> connection refused / admin prohibited
drop   -> timeout
```

---

# Stateful firewall

Stateful firewall помнит состояние соединений.

Для [[TCP]] он понимает:

```text
NEW
ESTABLISHED
RELATED
INVALID
```

Поэтому обычно разрешают входящие `ESTABLISHED,RELATED`, чтобы ответы на исходящие соединения возвращались обратно.

---

# Linux-инструменты

## nftables

Современная подсистема Linux firewall.

Показать правила:

```bash
sudo nft list ruleset
```

---

## iptables

Старый, но всё ещё очень распространённый интерфейс.

Показать rules:

```bash
sudo iptables -S
sudo iptables -t nat -S
```

---

## ufw

Упрощённая обёртка, часто на Ubuntu.

```bash
sudo ufw status verbose
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
```

---

# Cloud firewall

В cloud часто есть несколько уровней:

```text
instance firewall
security group
network ACL
load balancer rules
Kubernetes NetworkPolicy
```

Важно проверять все уровни, а не только `iptables` на сервере.

---

# Диагностика

Порт слушается локально:

```bash
sudo ss -lntp | grep ':443'
```

Порт доступен с другой машины:

```bash
nc -vz example.com 443
```

Проверить HTTP:

```bash
curl -v https://example.com
```

Проверить, приходят ли пакеты:

```bash
sudo tcpdump -i any port 443
```

Если пакеты не приходят — firewall/security group может быть до сервера.

Если SYN приходит, но ответа нет — проблема на сервере, route или local firewall.

---

# Частые ошибки

## Разрешили порт только на localhost

Firewall открыт, но приложение слушает:

```text
127.0.0.1:8080
```

Снаружи доступа не будет.

---

## Забыли UDP

DNS, WireGuard, QUIC и часть VPN работают по [[UDP]].

Открыть только TCP недостаточно.

---

## Заблокировали обратный трафик

Если firewall не stateful или rules собраны вручную, можно разрешить входящий SYN, но сломать ответы.

---

# Связанные заметки

- [[Network]]
- [[TCP]]
- [[UDP]]
- [[NAT]]
- [[VPN]]
- [[Security]]

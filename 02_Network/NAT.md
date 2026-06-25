# NAT

`NAT` — Network Address Translation, изменение IP-адреса или порта в пакете.

NAT чаще всего нужен, когда частная сеть должна ходить наружу через один публичный IP.

Связано с [[IPv4]], [[Routing]], [[Firewall]], Docker, Kubernetes и cloud networking.

---

# Зачем нужен NAT

Типичный пример:

```text
server: 10.0.1.15
internet: 8.8.8.8
public IP gateway: 203.0.113.10
```

Сервер с частным IP не маршрутизируется в интернете.

Gateway меняет source:

```text
10.0.1.15:51514 -> 203.0.113.10:40001
```

Ответ приходит на `203.0.113.10:40001`, gateway вспоминает mapping и отправляет ответ обратно на `10.0.1.15:51514`.

---

# SNAT

`SNAT` меняет source address.

Используется для исходящего трафика:

```text
private server -> internet
```

В Linux часто встречается как `MASQUERADE`.

Пример iptables:

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

---

# DNAT

`DNAT` меняет destination address.

Используется для входящего трафика:

```text
public IP:443 -> internal server:8443
```

Пример:

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 10.0.1.20:8443
```

---

# PAT

PAT — NAT с изменением port.

Именно он позволяет многим внутренним клиентам выходить в интернет через один публичный IP.

---

# Где NAT встречается

## Docker

При `-p 8080:80` Docker публикует порт контейнера на host.

Проверить:

```bash
docker ps
sudo iptables -t nat -S
```

---

## Kubernetes

`kube-proxy` использует NAT для Service traffic в iptables/IPVS режимах.

Связано:

- [[Kubernetes Service]]
- [[kube-proxy]]
- [[CNI]]

---

## Cloud

NAT Gateway даёт private subnet доступ в интернет без публичных IP на каждой VM.

---

# Диагностика

Показать NAT rules:

```bash
sudo iptables -t nat -S
sudo nft list ruleset
```

Посмотреть conntrack:

```bash
sudo conntrack -L
sudo conntrack -S
```

Проверить внешний IP:

```bash
curl ifconfig.me
curl https://api.ipify.org
```

Посмотреть пакеты до и после NAT:

```bash
sudo tcpdump -i any host 8.8.8.8
```

---

# Частые проблемы

## Нет обратного маршрута

DNAT настроен, запрос до backend доходит, но ответ уходит напрямую мимо NAT gateway.

Симптом:

```text
на backend SYN видно
клиент SYN-ACK не получает
```

---

## Закончился conntrack

При большом количестве соединений NAT state может переполниться.

Проверить:

```bash
sysctl net.netfilter.nf_conntrack_count
sysctl net.netfilter.nf_conntrack_max
```

---

## Hairpin NAT

Клиент из внутренней сети обращается к публичному IP, который DNAT-ится обратно внутрь.

Не все схемы поддерживают это без отдельной настройки.

---

# Связанные заметки

- [[Routing]]
- [[Firewall]]
- [[Docker Network]]
- [[Kubernetes Service]]
- [[tcpdump]]

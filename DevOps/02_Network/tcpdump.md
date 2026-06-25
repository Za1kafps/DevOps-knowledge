# tcpdump

`tcpdump` — утилита для просмотра сетевых пакетов на интерфейсе.

Она нужна, когда обычные команды говорят только “timeout”, “refused” или “не работает”, а нужно увидеть факт:

```text
пакет пришёл?
ответ ушёл?
какой IP/port?
есть SYN-ACK?
есть DNS response?
```

Связано с [[Network]], [[TCP]], [[UDP]], [[DNS]], [[Firewall]], [[Routing]].

---

# Базовая команда

```bash
sudo tcpdump -i any -nn
```

Флаги:

```text
-i any  слушать все интерфейсы
-n      не резолвить имена
-nn     не резолвить имена и порты
```

`-nn` важен: без него tcpdump может сам делать DNS-запросы и мешать диагностике.

---

# Фильтры

По host:

```bash
sudo tcpdump -i any -nn host 1.2.3.4
```

По port:

```bash
sudo tcpdump -i any -nn port 443
```

TCP:

```bash
sudo tcpdump -i any -nn tcp port 443
```

UDP:

```bash
sudo tcpdump -i any -nn udp port 53
```

Source/destination:

```bash
sudo tcpdump -i any -nn src host 10.0.1.10
sudo tcpdump -i any -nn dst host 10.0.1.10
```

---

# Проверить TCP handshake

```bash
sudo tcpdump -i any -nn 'tcp port 443'
```

Нормальный handshake:

```text
client > server: Flags [S]
server > client: Flags [S.]
client > server: Flags [.]
```

Только SYN без SYN-ACK:

```text
firewall drop
route back problem
service не отвечает
wrong destination
```

RST:

```text
порт закрыт
приложение/proxy сбросило соединение
```

---

# Проверить DNS

```bash
sudo tcpdump -i any -nn 'udp port 53 or tcp port 53'
```

Параллельно:

```bash
dig example.com
```

Так видно, уходит ли запрос к resolver и приходит ли ответ.

---

# Сохранить pcap

```bash
sudo tcpdump -i any -nn -w dump.pcap host 1.2.3.4
```

Открыть потом:

```bash
tcpdump -nn -r dump.pcap
```

Или в Wireshark.

---

# Смотреть payload

ASCII:

```bash
sudo tcpdump -i any -A -s 0 'tcp port 80'
```

Hex + ASCII:

```bash
sudo tcpdump -i any -X -s 0 'tcp port 80'
```

Для HTTPS payload будет зашифрован, но handshake и IP/ports всё равно видны.

---

# Частые ошибки

## Слушают не тот интерфейс

Если не уверен — начинай с:

```bash
sudo tcpdump -i any -nn
```

Потом сужай до конкретного interface.

---

## Забывают про NAT

До NAT и после NAT IP/port могут отличаться.

Иногда нужно слушать несколько интерфейсов.

---

## Делают вывод без `-n`

tcpdump начинает резолвить IP в имена, вывод становится медленнее и грязнее.

---

# Связанные заметки

- [[Network]]
- [[TCP]]
- [[UDP]]
- [[DNS]]
- [[Firewall]]
- [[Routing]]
- [[NAT]]

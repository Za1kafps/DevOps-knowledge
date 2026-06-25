# MTU

`MTU` — Maximum Transmission Unit, максимальный размер IP-пакета, который интерфейс может отправить без фрагментации.

Обычное значение для Ethernet:

```text
1500 bytes
```

MTU важен для [[VPN]], Docker overlay, Kubernetes CNI, VXLAN, cloud networking и [[UDP]].

---

# Почему MTU ломает сеть

Если пакет больше, чем можно передать по пути, должны произойти:

```text
fragmentation
или Path MTU Discovery
```

Но если ICMP-сообщения блокируются firewall, отправитель не узнаёт, что пакет надо уменьшить.

Симптом:

```text
маленькие запросы работают
большие зависают
TLS handshake странно ломается
curl подключается, но response не приходит
VPN работает нестабильно
```

---

# Проверка MTU

Показать MTU интерфейсов:

```bash
ip link
ip -br link
```

Проверить ping без фрагментации:

```bash
ping -M do -s 1472 8.8.8.8
```

Почему `1472`:

```text
1500 Ethernet MTU
- 20 IPv4 header
- 8 ICMP header
= 1472 payload
```

Для IPv6 overhead другой, поэтому проверять надо отдельно.

---

# tracepath

`tracepath` может показать path MTU:

```bash
tracepath example.com
```

Если где-то по пути MTU меньше, это будет видно в выводе.

---

# MTU и tunnels

Туннели добавляют overhead:

```text
WireGuard
OpenVPN
IPsec
VXLAN
GRE
```

Если физический интерфейс имеет MTU 1500, внутри туннеля полезная нагрузка должна быть меньше.

Пример:

```text
underlay MTU 1500
overlay MTU 1450 или меньше
```

---

# Kubernetes и MTU

CNI может использовать encapsulation.

Например VXLAN добавляет overhead, поэтому Pod MTU должен быть меньше underlay MTU.

Симптомы:

```text
pod-to-pod маленькие ответы работают
большие HTTP responses зависают
registry pull нестабилен
TLS ошибки без очевидной причины
```

Смотреть:

- [[CNI]]
- [[Cilium]]
- [[Calico]]
- [[Flannel]]

---

# Частые ошибки

## ICMP заблокирован

Path MTU Discovery зависит от ICMP.

Если firewall режет нужные ICMP-сообщения, получаются blackhole-соединения.

---

## MTU разный на overlay и underlay

Контейнерная сеть может пытаться отправить пакет, который не помещается после encapsulation.

---

## Проверяют только ping маленьким пакетом

Обычный `ping 8.8.8.8` не доказывает, что большие пакеты пройдут.

---

# Связанные заметки

- [[Network]]
- [[VPN]]
- [[UDP]]
- [[Docker Network]]
- [[Kubernetes Networking]]
- [[CNI]]

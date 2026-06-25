# UFW

`UFW` — простой firewall frontend для Linux, часто на Ubuntu.

Он управляет правилами netfilter/nftables через простой CLI.

---

# Базовая настройка

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

Проверить:

```bash
sudo ufw status verbose
```

---

# Правила

Разрешить порт:

```bash
sudo ufw allow 5432/tcp
```

Разрешить только с IP:

```bash
sudo ufw allow from 10.0.0.10 to any port 5432 proto tcp
```

Удалить:

```bash
sudo ufw delete allow 5432/tcp
```

---

# Осторожно с SSH

Перед `ufw enable` убедись, что SSH разрешён.

Иначе можно отрезать себе доступ.

---

# Docker и UFW

Docker может добавлять iptables rules, которые обходят ожидаемую UFW policy для published ports.

Проверять:

```bash
sudo iptables -S
sudo iptables -t nat -S
sudo ufw status verbose
```

---

# Связанные заметки

- [[Firewall]]
- [[OS Hardening]]
- [[Linux Server Setup]]

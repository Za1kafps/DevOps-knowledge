# Linux Server Setup

`Linux Server Setup` — базовая подготовка сервера к production-нагрузке.

---

# Минимальный порядок

```text
создать non-root user
настроить SSH keys
отключить password/root login
включить firewall
поставить updates
настроить time sync
поставить monitoring/logging
настроить backups
```

---

# Пользователь

```bash
adduser deploy
usermod -aG sudo deploy
```

SSH ключ:

```bash
mkdir -p /home/deploy/.ssh
chmod 700 /home/deploy/.ssh
```

---

# Проверки

```bash
hostnamectl
timedatectl
df -h
free -m
ss -lntp
systemctl --failed
journalctl -p err -b
```

---

# Security baseline

```text
SSH только ключи
UFW default deny
Fail2ban или VPN/bastion для SSH
автообновления security patches если подходит
минимум открытых ports
```

---

# Связанные заметки

- [[Linux]]
- [[SSH Hardening]]
- [[UFW]]
- [[Fail2ban]]
- [[OS Hardening]]

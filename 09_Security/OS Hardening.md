# OS Hardening

`OS Hardening` — уменьшение attack surface Linux-сервера.

Цель: если сервис уязвим или credential утёк, атакующему должно быть сложнее закрепиться и расширить доступ.

---

# Базовый checklist

```text
обновления безопасности
SSH only keys
root login disabled
firewall default deny inbound
минимум packages
отдельные users для сервисов
systemd sandboxing где возможно
logs/audit
fail2ban/rate limits для публичного SSH
```

---

# SSH

В `/etc/ssh/sshd_config`:

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

Проверить:

```bash
sudo sshd -t
sudo systemctl reload sshd
```

---

# Firewall

```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

Смотри [[UFW]].

---

# Updates

Debian/Ubuntu:

```bash
sudo apt update
sudo apt list --upgradable
```

Важно иметь процесс patching, а не ручное “когда вспомним”.

---

# Частые ошибки

## Hardening без доступа recovery

Можно отрезать SSH и потерять сервер.

## Открыт Docker socket

Доступ к `/var/run/docker.sock` почти равен root на host.

## Все сервисы от root

Компрометация сервиса сразу даёт слишком много.

---

# Связанные заметки

- [[Linux]]
- [[SSH Hardening]]
- [[UFW]]
- [[Fail2ban]]
- [[Audit Logs]]

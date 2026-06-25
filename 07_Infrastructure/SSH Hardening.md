# SSH Hardening

`SSH Hardening` — уменьшение риска компрометации SSH-доступа.

---

# Базовые настройки

В `/etc/ssh/sshd_config`:

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding no
AllowUsers deploy admin
```

Проверить конфиг:

```bash
sudo sshd -t
```

Reload:

```bash
sudo systemctl reload sshd
```

---

# Ключи

Предпочитать ed25519:

```bash
ssh-keygen -t ed25519
```

Права:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_ed25519
```

---

# fail2ban/rate limit

Если SSH доступен из интернета, добавить [[Fail2ban]] или ограничение по source IP/VPN.

Лучше:

```text
SSH только через VPN / bastion / ZeroTrust access
```

---

# Частые ошибки

## Менять SSH без второй сессии

Оставь активную сессию и проверь новый login перед logout.

## Один shared key на всех

Нельзя нормально отозвать доступ одному человеку.

## Root login

Лучше отдельный user + sudo.

---

# Связанные заметки

- [[SSH]]
- [[OS Hardening]]
- [[Fail2ban]]
- [[ZeroTrust]]

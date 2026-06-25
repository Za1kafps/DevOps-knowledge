# Fail2ban

`Fail2ban` читает logs и временно банит IP за повторяющиеся неуспешные попытки.

Часто используется для SSH brute force mitigation.

---

# Проверка

```bash
systemctl status fail2ban
fail2ban-client status
fail2ban-client status sshd
```

---

# Jail

Jail задаёт:

```text
какой log читать
какой filter применять
сколько попыток разрешить
на сколько банить
каким action банить
```

---

# Важно

Fail2ban не заменяет:

```text
SSH keys
password auth disabled
VPN/bastion
firewall allowlist
MFA/ZeroTrust access
```

---

# Частые ошибки

## Банит своих

Добавь trusted IP в ignoreip.

## Logs не совпадают с filter

Jail включён, но fail2ban ничего не видит.

## Считать fail2ban полной защитой

Это rate limiting, не strong auth.

---

# Связанные заметки

- [[SSH Hardening]]
- [[OS Hardening]]
- [[UFW]]

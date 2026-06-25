# Ansible

`Ansible` — инструмент configuration management и automation по SSH.

Terraform обычно создаёт инфраструктуру, Ansible настраивает OS и приложения внутри серверов.

---

# Основные понятия

```text
inventory  список hosts/groups
playbook   сценарий
play       набор tasks для hosts
task       вызов module
role       переиспользуемая структура
module     idempotent действие
handler    действие по notify
facts      данные о host
```

---

# Пример playbook

```yaml
- hosts: web
  become: true
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Ensure nginx is running
      systemd:
        name: nginx
        state: started
        enabled: true
```

Запуск:

```bash
ansible-playbook -i inventory.ini site.yml
```

---

# Idempotency

Хороший playbook можно запускать много раз.

Если состояние уже правильное, changes быть не должно.

Проверка:

```bash
ansible-playbook -i inventory.ini site.yml --check --diff
```

---

# Secrets

Для secrets:

```text
Ansible Vault
external secret manager
CI protected variables
```

Не хранить plaintext passwords в repo.

---

# Частые ошибки

## shell вместо module

`shell` часто не idempotent.

Лучше использовать `apt`, `template`, `copy`, `systemd`, `user`, `file`.

## Нет --diff/check в review

Перед production полезно понимать, что изменится.

## Inventory не разделён по окружениям

Можно случайно применить dev config к prod.

---

# Связанные заметки

- [[Infrastructure]]
- [[Linux Server Setup]]
- [[SSH]]
- [[Vault]]
- [[CI-CD]]

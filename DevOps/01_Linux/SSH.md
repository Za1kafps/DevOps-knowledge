# SSH

## Что это

`SSH` — протокол безопасного удаленного доступа к серверу.

Обычно используется для входа на сервер, выполнения команд, копирования файлов и создания туннелей.

Стандартный порт:

```
22
```

## Зачем нужен

SSH помогает:

подключаться к серверу  
управлять Linux удаленно  
копировать файлы  
пробрасывать порты  
работать с Git по SSH  
делать jump-подключения через промежуточный сервер

## Внутри как работает

SSH состоит из клиента и сервера.

Клиент:

```
ssh
```

Сервер:

```
sshd
```

Основные части SSH:

аутентификация  
шифрование  
ключи  
known_hosts  
authorized_keys  
ssh-agent  
конфиг клиента  
конфиг сервера

## Основные файлы

Клиентские файлы:

```
~/.ssh/id_rsa
~/.ssh/id_ed25519
~/.ssh/id_rsa.pub
~/.ssh/id_ed25519.pub
~/.ssh/known_hosts
~/.ssh/config
```

Серверные файлы:

```
/etc/ssh/sshd_config
~/.ssh/authorized_keys
/var/log/auth.log
```

## Подключение

```
ssh user@server
```

Подключение на другой порт:

```
ssh -p 2222 user@server
```

Подключение с конкретным ключом:

```
ssh -i ~/.ssh/id_ed25519 user@server
```

## SSH-ключи

Создать ключ:

```
ssh-keygen -t ed25519
```

Скопировать ключ на сервер:

```
ssh-copy-id user@server
```

Проверить публичный ключ:

```
cat ~/.ssh/id_ed25519.pub
```

Права на SSH-файлы:

```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
```

## SSH config

Файл:

```
~/.ssh/config
```

Пример:

```
Host prod
    HostName 1.2.3.4
    User root
    Port 22
    IdentityFile ~/.ssh/id_ed25519
```

После этого можно подключаться так:

```
ssh prod
```

## Проверка SSH-сервиса

```
sudo systemctl status ssh
sudo systemctl status sshd
```

На разных дистрибутивах сервис может называться по-разному:

```
ssh
sshd
```

Проверить, слушает ли SSH порт:

```
sudo ss -lntp | grep ':22'
```

Проверить конфиг sshd:

```
sudo sshd -t
```

Перезапустить SSH:

```
sudo systemctl restart ssh
```

или:

```
sudo systemctl restart sshd
```

## Логи SSH

Debian/Ubuntu:

```
sudo journalctl -u ssh
sudo tail -f /var/log/auth.log
```

RHEL/CentOS:

```
sudo journalctl -u sshd
sudo tail -f /var/log/secure
```

## Плюсы

безопасный удаленный доступ  
шифрование трафика  
можно работать без пароля через ключи  
можно пробрасывать порты  
удобно для Git, серверов и DevOps  
можно использовать jump-host

## Минусы

если потерять ключ — можно потерять доступ  
если открыть парольный вход наружу — можно ловить brute force  
неправильные права на `~/.ssh` ломают вход  
ошибки в `sshd_config` могут отрезать доступ  
не стоит перезапускать SSH без проверки конфига

```

telnet не безопасен и почти не используется для управления серверами.

## Важные недочеты

Перед рестартом SSH всегда проверять конфиг:

```
sudo sshd -t
```

Лучше не закрывать текущую SSH-сессию, пока не проверил новую.

Если поменял порт SSH, надо проверить firewall:

```
sudo ufw status
sudo iptables -S
sudo nft list ruleset
```

Если ошибка:

```
Permission denied (publickey)
```
Проверить:

ключ на клиенте  
ключ в authorized_keys
права на .ssh
пользователя  
порт  
логи сервера
```
[[Linux]]  
[[Network]] 
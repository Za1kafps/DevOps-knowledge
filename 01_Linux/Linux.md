# Linux

Связано: [[DevOps]]
## Что это

[[Linux]] — это семейство свободных операционных систем с открытым исходным кодом, основанных на ядре **Linux**, разработанном Линусом Торвальдсом.
## Основные части

Hardware → Kernel → System libraries → Shell/systemd → Applications
## Kernel

Ядро управляет процессами, памятью, сетью, дисками и драйверами.

`uname -r` — версия ядра
## Пользователи и права

`whoami` — текущий пользователь  
`id` — группы пользователя  
`ls -l` — права файлов

Права:

`r` — read  
`w` — write  
`x` — execute
## Сервисы

`systemctl status nginx` — статус  
`sudo systemctl start nginx` — запустить  
`sudo systemctl stop nginx` — остановить  
`sudo systemctl restart nginx` — перезапустить  
`sudo systemctl enable nginx` — включить автозапуск

Логи:
```bash
journalctl -u nginx
```
## Процессы
```bash
ps aux  
top  
htop  
pgrep nginx  
kill PID
```
## Сеть

`ip a` — IP-адреса  
`ip route` — маршруты  
`ss -tulpn` — открытые порты  
`ping 8.8.8.8` — проверка сети  
`curl -v https://example.com` — проверка HTTP  
`dig example.com` — DNS

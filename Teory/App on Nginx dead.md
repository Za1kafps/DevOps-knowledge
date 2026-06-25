### Error Status: 502/504/500/connection refused
#### command to test status
```bash
curl -v http://example.com
curl -vk http://example.com

systemctl status nginx
nginx -t
journalctl -u nginx -n 100 --no-pager

tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

ss -lntp

systemctl status APP
journalctl -u APP -n 100 --no-pager
```

##### 502 Bad Gateway
Nginx живой, но backend недоступен.
Причины:
- backend не запущен
- backend слушает другой порт
- backend слушает только 127.0.0.1
- ошибка proxy_pass
- upsteam умер
- connection refused
Проверка: 
```bash
nginx -T | grep proxy_pass
ss -lntp
curl -v http://127.0.0.1:3000
systemctl status APP
journalctl -u APP -n 100 --no-pager
```
##### 504 Gateway Timeout
Nginx достучался до backend, но backend долго не отвечает.
Причины:
- backend завис
- долгий запрос в базу
- проблема с внешним API
- deadlock
- медленный disk I/O (деградация)
- перегрузка CPU/RAM
Проверка:
```bash
top
free -h
iostat -xz 1
journalctl -u APP -n 100 --no-pager
strace -p <PID>
```
##### 500 Internal Server Error
Проблема внутри приложения или конфигов
Проверка:
```bash
journalctl -u APP -n 100 --no-pager
docker logs <container>
kubectl logs <pod> -n <namespace> 
```
##### 403 Forbidden
Причины:
- нет прав на файл
- nginx deny rule
- нет index.html
- autoindex off
- SELinux/AppArmor
Проверки:
```bash
ls -l /var/www/site
namei -l /var/www/site/index.html
nginx -T
tail -100 /var/log/nginx/error.log
```
##### 404 Not Found
Причины:
- не тот server_name
- не тот location
- не тот root
- не то тproxdy_pass
- приложение само вернуло 404
Проверки:
```bash
nginx -T
curl -v http://127.0.0.1:300/path
tail -f /var/log/nginx/access.log
```
[[App on Nginx dead]], [[Inode]], [[Load average]], [[Logic of troubleshooting]], [[PID]], [[ports]], [[protocols]], [[DevOps/Teory/strace|strace]] 
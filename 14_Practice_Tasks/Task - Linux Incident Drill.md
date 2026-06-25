# Task - Linux Incident Drill

## Ситуация

На сервере выросла latency, часть requests возвращает 5xx, deploy не выполнялся. За 15 минут нужно определить ограничивающий ресурс и восстановить service.

## Первые команды

```bash
date -Is
uptime
systemctl --failed
journalctl -p warning..alert --since -30m
free -h
vmstat 1
mpstat -P ALL 1
iostat -xz 1
df -hT
df -ih
ss -s
```

## Процессы

```bash
ps -eo pid,ppid,user,stat,%cpu,%mem,rss,etime,cmd --sort=-%cpu | head
pidstat -dur 1
systemctl status app
journalctl -u app --since -30m
cat /proc/<pid>/limits
cat /proc/<pid>/status
```

## Network

```bash
ss -lntp
ss -tan state syn-recv
ip -s link
ip route
dig api.example.com
curl -sv --connect-timeout 3 http://127.0.0.1:8080/health
```

## Сценарии

- CPU saturation одним process;
- memory pressure и OOM kill;
- disk latency;
- filesystem заполнен удалённым, но открытым log file;
- inode exhaustion;
- file descriptor exhaustion;
- listen backlog/SYN queue;
- DNS timeout;
- dependency connection pool exhausted.

## Правило

Не перезапускай service до сохранения минимального набора фактов, если impact позволяет. Restart может восстановить service и одновременно уничтожить состояние, нужное для root cause.

## Критерий готовности

- bottleneck подтверждён двумя независимыми signals;
- найден процесс/cgroup/device/dependency;
- mitigation уменьшил impact;
- после recovery проверены latency, errors и saturation;
- описана автоматическая alert.

## Связи

- [[Incident Command Map]]
- [[Linux High CPU]]
- [[High CPU]]
- [[OOMKilled]]
- [[Linux Processes]]
- [[Troubleshooting]]

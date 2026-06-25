# Incident Command Map

Команды выбирают по слою проблемы. Большой случайный dump замедляет поиск и может создать дополнительную нагрузку.

## Linux overview

```bash
date -Is
uptime
systemctl --failed
journalctl -p warning..alert --since -30m
```

## CPU и scheduler

```bash
mpstat -P ALL 1
pidstat -u 1
ps -eo pid,ppid,stat,%cpu,comm --sort=-%cpu | head
vmstat 1
```

Смотри user/system/iowait/steal, run queue и throttling cgroup.

## Memory

```bash
free -h
vmstat 1
cat /proc/meminfo
ps -eo pid,rss,vsz,%mem,cmd --sort=-rss | head
journalctl -k | rg -i 'oom|killed process'
```

## Disk

```bash
df -hT
df -ih
du -xhd1 /var | sort -h
lsof +L1
iostat -xz 1
```

`df` и `du` расходятся при удалённом открытом файле, hidden mount или reserved blocks.

## Network

```bash
ip -br addr
ip route
ip rule
ip neigh
ss -s
ss -lntp
ss -tan state syn-recv
ethtool -S <iface>
tcpdump -ni any host <ip> and port <port>
```

## DNS и HTTP/TLS

```bash
getent ahosts <name>
dig <name>
curl -sv --connect-timeout 3 --max-time 15 <url>
openssl s_client -connect <host>:443 -servername <host>
```

## Containers

```bash
docker ps -a
docker inspect <container>
docker logs --since 30m <container>
docker stats --no-stream
crictl ps -a
crictl pods
crictl logs <container-id>
```

## Kubernetes

```bash
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> -c <container> --previous
kubectl get svc,endpointslice -n <ns>
kubectl auth can-i --list -n <ns>
```

## PostgreSQL

```sql
SELECT now(), pg_is_in_recovery();
SELECT * FROM pg_stat_activity;
SELECT * FROM pg_stat_replication;
SELECT * FROM pg_locks WHERE NOT granted;
```

## После mitigation

Повтори исходный пользовательский request и проверь golden signals:

```text
latency
traffic
errors
saturation
```

## Связи

- [[Incident Response Flow]]
- [[Troubleshooting]]
- [[Metrics]]
- [[Logs]]
- [[Tracing]]

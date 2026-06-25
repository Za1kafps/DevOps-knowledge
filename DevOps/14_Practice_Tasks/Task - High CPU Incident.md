# Task - High CPU Incident

## Симптом

Load average и latency выросли, CPU близок к 100%.

## Диагностика

```bash
uptime
mpstat -P ALL 1
pidstat -u -t 1
ps -eo pid,ppid,stat,psr,%cpu,etime,cmd --sort=-%cpu | head -20
vmstat 1
```

Различай:

- один busy process;
- много runnable processes;
- kernel/system CPU;
- iowait;
- steal time VM;
- cgroup CPU throttling.

Для systemd cgroup:

```bash
systemd-cgtop
systemctl show app -p CPUQuotaPerSecUSec
```

Для процесса:

```bash
top -H -p <pid>
pidstat -p <pid> -t 1
perf top -p <pid>
```

## Сценарии

- бесконечный loop;
- regex backtracking;
- слишком высокий worker concurrency;
- compression/encryption burst;
- GC pressure;
- CPU limit/throttling container;
- traffic spike.

## Критерий готовности

Нельзя завершать задачу выводом “CPU высокий”. Нужно назвать process/thread/function или cgroup limit, связать его с latency и проверить recovery после mitigation.

## Связи

- [[Linux High CPU]]
- [[High CPU]]
- [[Capacity Planning]]
- [[Resources Requests and Limits]]

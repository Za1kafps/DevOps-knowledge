# node_exporter

`node_exporter` экспортирует Linux host metrics для Prometheus.

Он показывает состояние node/VM:

```text
CPU
memory
filesystem
disk IO
network
load
system time
process counts
```

---

# Проверка

```bash
curl http://localhost:9100/metrics
```

В Prometheus:

```promql
up{job="node-exporter"}
```

---

# Полезные метрики

CPU:

```promql
rate(node_cpu_seconds_total[5m])
```

Memory:

```promql
node_memory_MemAvailable_bytes
```

Filesystem:

```promql
node_filesystem_avail_bytes
```

Disk IO:

```promql
rate(node_disk_read_bytes_total[5m])
rate(node_disk_written_bytes_total[5m])
```

---

# Частые проблемы

## Filesystem alerts на pseudo fs

Нужно исключать tmpfs, proc, sysfs, overlay где неуместно.

## exporter down

Проверить systemd, firewall, scrape config.

## host metrics без labels

Добавь environment/cluster/role labels на scrape level.

---

# Связанные заметки

- [[Prometheus]]
- [[Metrics]]
- [[Capacity Planning]]

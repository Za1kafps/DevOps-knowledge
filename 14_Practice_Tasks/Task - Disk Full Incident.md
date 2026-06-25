# Task - Disk Full Incident

## Симптом

Приложение не пишет данные, PostgreSQL останавливается или container runtime не скачивает image:

```text
No space left on device
```

## Диагностика

```bash
df -hT
df -ih
findmnt
lsblk -f
du -xhd1 /var | sort -h
lsof +L1
journalctl --disk-usage
```

Проверяй отдельно bytes и inodes. Миллионы маленьких файлов могут исчерпать inode при свободных гигабайтах.

`lsof +L1` показывает удалённые, но открытые файлы. Место освободится после закрытия descriptor/restart процесса; не обрезай `/proc/<pid>/fd/*` без понимания приложения.

## Сценарии

- journald без ограничений;
- container logs растут;
- deleted log удерживается process;
- inode exhaustion;
- Docker/containerd image layers;
- PostgreSQL WAL растёт из-за broken archive/replication slot;
- filesystem read-only после I/O errors.

## Mitigation

Сначала останови рост, затем освободи безопасное место. Не удаляй database files, active WAL или runtime snapshots вручную.

## Проверка

```bash
journalctl --vacuum-size=1G
docker system df
crictl images
```

Cleanup images выполняй только с пониманием, какие runtime/containers их используют.

## Связи

- [[Linux Filesystem]]
- [[Logs]]
- [[WAL]]
- [[Container Runtime and CRI]]
- [[Database Monitoring]]

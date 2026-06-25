load average — среднее количество процессов, которые выполняются или ждут CPU/I/O
watch on:
- uptime
- top
- htop
- cat /proc/loadavg
Load может быть высоким не только из-за CPU, процессы в состоянии D которые ждут disk I/O, тоже его увеличивают 
```bash
top
vmstat 1
iostat -xz 1
pidstat 1
```
[[App on Nginx dead]], [[Inode]], [[Load average]], [[Logic of troubleshooting]], [[PID]], [[ports]], [[protocols]], [[DevOps/Teory/strace|strace]] 
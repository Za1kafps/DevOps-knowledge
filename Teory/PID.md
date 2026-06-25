### PID — это process ID, уникальный номер процесса LInux
--- 
Узнать PID через ps или grep:
```bash
ps aux | grep APP
ps aux } grep '[A]PP'
pgrep APP
pgrep -af APP
```
Узнать PID через systemd
```bash
systemctl status APP
```
узнать PID 
[[App on Nginx dead]], [[Inode]], [[Load average]], [[Logic of troubleshooting]], [[PID]], [[ports]], [[protocols]], [[DevOps/Teory/strace|strace]] 
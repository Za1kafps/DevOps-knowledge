strace показывает системные вызови процессов, приложение не может напрямую открыть файл, создать сокет или подключится к сети. Происходит запрос к ядру Linux через syscall
#### syscall примеры
- openat()
- read()
- write()
- bind()
- accept()
######
Установка strace происходит через
```bash
sudo apt install strace
```
---
##### Использование strace:
Запустить приложение под strace
```bash
strace ./app
strace -o trace.log ./app (для записи в файл)
strace -f -ttT -s 256 -o trace.log ./app (universal use)
```

- `ENOENT` — файл не найден
- `EACCES` — нет прав доступа
- `ECONNREFUSED` — соединение отклонено
- `ETIMEDOUT` — тайм-аут соединения
- `EADDRINUSE` — порт уже занят
- `EMFILE` — слишком много открытых файлов
- `ENOMEM` — не хватает памяти
- `Permission denied` — проблема с правами
- `No such file or directory` — нет файла или директории
сводка syscall:
```bash
strace -c ./app
```
#### Format:
> syscall(arguments) = result 
Example
```bash
openat(AT-FDCWD, "/ect/passwd", O_RDONLY) = 3
```
######
### File descriptors
- 0 — stdin
- 1 — stdout
- 2 — stderr
- 3+ — файлы, сокеты, pipe, и другие объекты
 
[[App on Nginx dead]], [[Inode]], [[Load average]], [[Logic of troubleshooting]], [[PID]], [[ports]], [[protocols]], [[DevOps/Teory/strace|strace]] 
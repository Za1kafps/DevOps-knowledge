# Linux Filesystem

Связано: [[Linux]], [[Permissions]]

## Что это

Linux Filesystem — структура файлов и директорий в [[Linux]].
## Важные директории

`/etc` — конфиги  
`/var` — логи и данные сервисов  
`/home` — пользователи  
`/root` — home root  
`/usr` — программы и библиотеки  
`/bin` — базовые команды  
`/tmp` — временные файлы  
`/proc` — процессы и ядро  
`/dev` — устройства  
`/mnt` — точки монтирования  
`/boot` — загрузчик и kernel

## Права

`ls -l`

Пример:

`-rwxr-xr--`

Расшифровка:

user: `rwx`  
group: `r-x`  
others: `r--`

## chmod

`chmod +x script.sh`  
`chmod 644 file.txt`  
`chmod 755 script.sh`

Часто:

`644` — обычный файл  
`755` — скрипт или директория  
`600` — приватный файл  
`700` — приватная директория

## chown

`sudo chown user:user file.txt`  
`sudo chown -R user:user /path`

## Диски и место

`df -h` — свободное место  
`du -sh *` — размер файлов/папок  
`lsblk` — диски  
`findmnt` — точки монтирования

## Поиск

`find / -name "nginx.conf" 2>/dev/null`  
`find / -type f -size +1G 2>/dev/null`

## Частые проблемы

Нет места:

`df -h`  
`du -sh /*`  
`du -sh /var/log/*`

Нет прав:

`ls -l file`  
`id`  
`namei -l /path/to/file`

Read-only filesystem:

`mount | grep " ro,"`  
`journalctl -k -b`
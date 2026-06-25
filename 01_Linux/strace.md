# strace

## Что это

`strace` — утилита для трассировки системных вызовов процесса в [[Linux]].

Она показывает, как программа общается с ядром.

Пример:

программа открывает файл  
программа читает конфиг  
программа подключается к порту  
программа получает ошибку permission denied  
программа не может найти библиотеку

## Зачем нужен

`strace` помогает понять:

какой файл ищет программа  
почему ошибка `No such file or directory`  
почему ошибка `Permission denied`  
куда программа подключается  
какие системные вызовы падают  
на чем процесс завис  
какие файлы и сокеты реально использует приложение

## Внутри как работает

`strace` использует механизм ядра:

```
ptrace
```

`ptrace` позволяет одному процессу наблюдать за другим процессом.

`strace` не дебажит код как IDE. Он показывает системные вызовы.

Пример системных вызовов:

```
openat()
read()
write()
connect()
accept()
stat()
execve()
clone()
mmap()
```
## Основные команды

Запустить программу под strace:

```
strace ./app
```

Подключиться к уже запущенному процессу:

```
sudo strace -p PID
```

Сохранить вывод в файл:

```
strace -o trace.log ./app
```

Показать только файлы:

```
strace -e trace=file ./app
```

Показать только сеть:

```
strace -e trace=network ./app
```

Показать только процессы:

```
strace -e trace=process ./app
```

Показать время вызовов:

```
strace -tt ./app
```

Показать длительность системных вызовов:

```
strace -T ./app
```

Следить за дочерними процессами:

```
strace -f ./app
```

Краткая статистика:

```
strace -c ./app
```

## Частые кейсы

Найти, какой конфиг ищет программа:

```
strace -e trace=file ./app 2>&1 | grep config
```

Понять, почему файл не открывается:

```
strace -e trace=file ./app
```

Проверить сетевые подключения:

```
strace -e trace=network ./app
```

Подключиться к зависшему процессу:

```
sudo strace -p PID
```
## Частые ошибки

```
ENOENT       No such file or directory
EACCES       Permission denied
ECONNREFUSED Connection refused
ETIMEDOUT    Connection timed out
EADDRINUSE   Address already in use
EMFILE       Too many open files
ENOMEM       Cannot allocate memory
```

## Пример чтения вывода

```
openat(AT_FDCWD, "/etc/app/config.yaml", O_RDONLY) = -1 ENOENT
```

Это значит:

программа пыталась открыть `/etc/app/config.yaml`  
ядро ответило `ENOENT`  
файл не найден

Пример:

```
connect(3, {sa_family=AF_INET, sin_port=htons(5432), sin_addr=inet_addr("10.0.0.5")}, 16) = -1 ECONNREFUSED
```

Это значит:

программа пыталась подключиться к `10.0.0.5:5432`  
соединение отклонено  
скорее всего порт закрыт или сервис не слушает

## Важные недочеты

Если приложение запускает дочерние процессы, нужен флаг:

```
-f
```

Если не использовать `-f`, можно не увидеть важную часть работы.

Если вывод идет в stderr, это нормально. У `strace` вывод по умолчанию идет в stderr.

Поэтому часто используют:

```
strace ./app 2>&1
```

## Связано с

[[Linux]]  
[[Troubleshooting]]  
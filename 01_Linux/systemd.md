# systemd

## Что это

`systemd` — система инициализации и управления сервисами в [[Linux]].

Это первый основной процесс пользовательского пространства.

Обычно имеет PID 1.

Проверить:

```
ps -p 1 -o comm=
```

## Зачем нужен

`systemd` управляет:

запуском системы  
сервисами  
зависимостями  
логами через journal  
таймерами  
mount-ами  
сокетами  
лимитами процессов  
cgroups  
автозапуском сервисов

## Внутри как работает

Главная идея systemd — units.

Unit — объект, которым управляет systemd.

Основные типы units:

```
.service   сервис
.socket    сокет
.timer     таймер
.target    группа units
.mount     mount-точка
.path      запуск по изменению файла
.device    устройство
```

## Основные команды

Статус сервиса:

```
systemctl status nginx
```

Запустить сервис:

```
sudo systemctl start nginx
```

Остановить сервис:

```
sudo systemctl stop nginx
```

Перезапустить сервис:

```
sudo systemctl restart nginx
```

Перечитать конфиги systemd:

```
sudo systemctl daemon-reload
```

Включить автозапуск:

```
sudo systemctl enable nginx
```

Отключить автозапуск:

```
sudo systemctl disable nginx
```

Включить и сразу запустить:

```
sudo systemctl enable --now nginx
```

Отключить и сразу остановить:

```
sudo systemctl disable --now nginx
```

## Логи

Логи сервиса:

```
journalctl -u nginx
```

Логи сервиса за текущую загрузку:

```
journalctl -u nginx -b
```

Логи в live-режиме:

```
journalctl -u nginx -f
```

Последние 100 строк:

```
journalctl -u nginx -n 100
```

Логи ядра:

```
journalctl -k
```

Логи ядра за текущую загрузку:

```
journalctl -k -b
```

## Unit-файлы

Посмотреть unit:

```
systemctl cat nginx
```

Где лежат unit-файлы:

```
/etc/systemd/system/
/usr/lib/systemd/system/
/lib/systemd/system/
```

Обычно свои правки лучше делать через override:

```
sudo systemctl edit nginx
```

После правок:

```
sudo systemctl daemon-reload
sudo systemctl restart nginx
```

## Пример service unit

```
[Unit]
Description=My App
After=network.target

[Service]
ExecStart=/opt/myapp/app
WorkingDirectory=/opt/myapp
Restart=always
RestartSec=5
User=myapp
Group=myapp

[Install]
WantedBy=multi-user.target
```

## Важные параметры service

```
ExecStart=       команда запуска
WorkingDirectory= рабочая директория
User=            пользователь
Group=           группа
Restart=         политика рестарта
RestartSec=      пауза перед рестартом
Environment=     переменные окружения
EnvironmentFile= файл с переменными
LimitNOFILE=     лимит открытых файлов
MemoryMax=       лимит памяти
CPUQuota=        лимит CPU
After=           стартовать после unit
Requires=        жесткая зависимость
Wants=           мягкая зависимость
WantedBy=        куда устанавливается автозапуск
```

## Проверка проблем

Проверить статус:

```
systemctl status service-name
```

Проверить логи:

```
journalctl -u service-name -b -n 100
```

Проверить unit:

```
systemctl cat service-name
```

Проверить зависимости:

```
systemctl list-dependencies service-name
```

Проверить ошибки загрузки:

```
systemctl --failed
```
## Частые кейсы

Сервис не стартует:

```
systemctl status app
journalctl -u app -b -n 100
systemctl cat app
```

После изменения unit-файла сервис не видит изменения:

```
sudo systemctl daemon-reload
sudo systemctl restart app
```

Сервис постоянно перезапускается:

```
systemctl status app
journalctl -u app -f
```

Сервис уперся в лимит файлов:

```
systemctl cat app | grep LimitNOFILE
cat /proc/PID/limits
```

Если сервис упал, сначала смотреть:

```
systemctl status service-name
journalctl -u service-name -b -n 100
```
## Полезные вещи

Посмотреть PID сервиса:

```
systemctl show -p MainPID nginx
```

Посмотреть окружение сервиса:

```
systemctl show nginx
```

Проверить, включен ли автозапуск:

```
systemctl is-enabled nginx
```

Проверить, активен ли сервис:

```
systemctl is-active nginx
```

Показать все failed units:

```
systemctl --failed
```

Сбросить failed-состояние:

```
sudo systemctl reset-failed
```

## Связано с

[[Linux]] 
[[Troubleshooting]]
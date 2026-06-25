# journalctl

Связано: [[Linux]], [[Logs]], [[Troubleshooting]]

## Что это

`journalctl` — команда для просмотра логов `systemd`.

Используется для диагностики сервисов, системы и ядра.

## Основные команды

`journalctl` — все логи  
`journalctl -u nginx` — логи сервиса  
`journalctl -u nginx -f` — смотреть live  
`journalctl -u nginx -n 100` — последние 100 строк

## Логи загрузки

`journalctl -b` — текущая загрузка  
`journalctl -b -1` — прошлая загрузка  
`journalctl --list-boots` — список загрузок

## Ошибки

`journalctl -p err` — только ошибки  
`journalctl -p err -b` — ошибки за текущую загрузку

## Kernel logs

`journalctl -k`  
`journalctl -k -b`

Полезно для проблем с драйверами, дисками, сетью, OOM Killer.

## По времени

`journalctl --since "1 hour ago"`  
`journalctl --since "today"`  
`journalctl -u nginx --since "30 minutes ago"`

## Типовой сценарий

`systemctl status nginx`  
`journalctl -u nginx -n 100`  
`journalctl -u nginx -f`

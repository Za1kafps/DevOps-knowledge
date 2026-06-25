# curl

`curl` — это консольная утилита для отправки HTTP/HTTPS-запросов, относится к [[Network]]

Её используют, чтобы проверить сайт, API, сервер, Ingress, Nginx, редиректы, заголовки и ошибки.

Общий вид:

```bash
curl https://example.com
```

По умолчанию `curl` отправляет [[GET]]-запрос и выводит ответ в терминал.
	
---

# Основные команды

## Обычный запрос

```bash
curl https://example.com
```

Получить ответ от сайта или API.

---

## Подробный вывод

```bash
curl -v https://example.com
```

`-v` показывает больше информации:

```text
DNS
подключение к IP
TLS/SSL
заголовки запроса
заголовки ответа
```

Полезно для диагностики.

---

## Сохранить ответ в файл

```bash
curl -o page.html https://example.com
```

`-o` сохраняет ответ в файл.

---

## Скачать файл

```bash
curl -O https://example.com/file.zip
```

`-O` скачивает файл с оригинальным именем.

---

# Отправка данных

## [[POST]]-запрос

```bash
curl -d "name=Ivan" https://example.com/api/users
```

`-d` отправляет данные в теле запроса.

При использовании `-d` curl автоматически делает `POST`.

---

## [[POST]] JSON

```bash
curl -X POST https://example.com/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ivan"}'
```

Используется для API.

---

## Добавить заголовок

```bash
curl -H "Accept: application/json" https://example.com/api
```

`-H` добавляет HTTP-заголовок.

---

## Авторизация через токен

```bash
curl -H "Authorization: Bearer TOKEN" https://example.com/api/profile
```

Используется для API с Bearer Token.

---

## Basic Auth

```bash
curl -u user:password https://example.com/admin
```

`-u` передаёт логин и пароль.

---
## Проверить сайт подробно

```bash
curl -v https://example.com
```

Сразу видно, дошёл ли запрос до сервера и что сервер ответил.

---

## Проверить HTTPS без проверки сертификата

```bash
curl -vk https://example.com
```

`-k` отключает строгую проверку TLS-сертификата.

Полезно для тестовых серверов, self-signed сертификатов и Ingress.

---

## Проверить конкретный IP под доменом

```bash
curl -vk --resolve example.com:443:1.2.3.4 https://example.com
```

`--resolve` подменяет [[DNS]] только для этого запроса.

То есть запрос идёт на IP `1.2.3.4`, но домен остаётся `example.com`.

Полезно, если [[DNS]] ещё не переключён или нужно проверить конкретный сервер.

---

## Проверить [[Ingress]]/[[Nginx]] по Host

```bash
curl -v -H "Host: example.com" http://1.2.3.4
```

Запрос идёт на IP, но сервер видит домен `example.com`.

Полезно для проверки virtual host, Nginx или Kubernetes Ingress.

---

## Показать только HTTP-код

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

Пример вывода:

```text
200
```

Полезно для быстрой проверки доступности. [[Response HTTP States]]

---

## Показать HTTP-код и время ответа

```bash
curl -s -o /dev/null -w "code=%{http_code} time=%{time_total}\n" https://example.com
```

Пример:

```text
code=200 time=0.231
```

---

# Частые опции

|Опция|Что делает|
|---|---|
|`-d`|Отправить данные|
|`-f`|Считать HTTP 400/500 ошибкой|
|`-i`|Показать заголовки и тело|
|`-I`|Показать только заголовки|
|`-o`|Сохранить ответ в файл|
|`-O`|Скачать файл с оригинальным именем|
|`-s`|Тихий режим|
|`-u`|Логин и пароль|
|`-A`|Указать User-Agent|
|`-v`|Подробный вывод|
|`-H`|Добавить заголовок|
|`-X`|Указать HTTP-метод|
|`-k`|Не проверять TLS-сертификат|
|`-L`|Следовать редиректам|
|`--resolve`|Подменить DNS для запроса|
|`-w`|Вывести HTTP-код, время и другие метрики|

---

# Что можно понять через curl

С помощью `curl` можно быстро проверить:

```text
домен резолвится или нет
порт открыт или нет
HTTPS работает или нет
сертификат нормальный или нет
сервер отвечает или нет
какой HTTP-код приходит
есть ли редирект
работает ли API endpoint
Ingress/Nginx прокидывает запрос или нет
```

Основные команды для начала диагностики:

```bash
curl -v https://example.com
```

```bash
curl -I https://example.com
```

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```
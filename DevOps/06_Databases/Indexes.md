# Indexes

`Index` ускоряет чтение, но замедляет запись и занимает место.

В PostgreSQL индекс нужен, когда запросы часто фильтруют, сортируют или join-ят по колонкам.

---

# Проверка query plan

```sql
explain analyze
select * from users where email = 'a@example.com';
```

Смотреть:

```text
Seq Scan
Index Scan
Bitmap Index Scan
rows estimate vs actual
cost
execution time
```

---

# Создание

Для production больших таблиц:

```sql
create index concurrently idx_users_email on users(email);
```

Обычный `create index` может блокировать writes.

---

# Частые ошибки

## Индекс на всё подряд

Каждый индекс увеличивает стоимость insert/update/delete.

## Неверный порядок composite index

Индекс `(a, b)` не равен `(b, a)`.

## Функция ломает использование индекса

Например `where lower(email) = ...` требует functional index.

---

# Связанные заметки

- [[PostgreSQL]]
- [[Database Migrations]]
- [[Database Monitoring]]

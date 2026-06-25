# Database Restore Drill

`Database Restore Drill` — тренировочное восстановление базы из backup.

Цель — доказать, что backup реально работает и укладывается в RTO/RPO.

---

# Что проверять

```text
backup доступен
backup не битый
есть ключи расшифровки
restore procedure понятна
данные консистентны
приложение запускается на restored DB
время restore измерено
```

---

# PostgreSQL пример

```bash
createdb restore_test
pg_restore -d restore_test appdb.dump
psql -d restore_test -c "select count(*) from important_table;"
```

---

# Результат drill

Записать:

```text
backup timestamp
restore duration
errors
manual steps
data validation
что улучшить
```

---

# Частые находки

```text
нет роли/extension
backup неполный
restore слишком долгий
нет доступа к bucket
ключ шифрования неизвестен
runbook устарел
```

---

# Связанные заметки

- [[Database Backups]]
- [[RTO and RPO]]
- [[Disaster Recovery]]

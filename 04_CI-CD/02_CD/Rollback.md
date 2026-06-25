# Rollback

`Rollback` — возврат системы к предыдущей рабочей версии или состоянию.

Rollback должен быть частью CD заранее, а не импровизацией во время инцидента.

---

# Что можно откатывать

```text
application version
container image
Kubernetes Deployment revision
Helm release
configuration
feature flag
database migration
traffic routing
```

Не всё откатывается одинаково. Код откатить проще, данные — сложнее.

---

# Kubernetes rollback

История:

```bash
kubectl rollout history deploy/app -n production
```

Откат:

```bash
kubectl rollout undo deploy/app -n production
```

Откат к revision:

```bash
kubectl rollout undo deploy/app -n production --to-revision=3
```

Проверка:

```bash
kubectl rollout status deploy/app -n production
```

---

# Helm rollback

```bash
helm history app -n production
helm rollback app 3 -n production
```

Если Helm управляется Flux/Argo CD, ручной rollback может быть перетёрт GitOps controller.

В GitOps правильнее вернуть desired state в Git.

---

# GitOps rollback

В GitOps rollback обычно:

```text
revert commit
merge
controller applies previous desired state
```

Плюс: audit trail остаётся в Git.

Минус: rollback зависит от скорости review/merge/reconcile, если нет emergency process.

---

# База данных

DB rollback сложнее всего.

Опасно:

```text
drop column
rename column
change type
data destructive migration
```

Для production нужны backward-compatible migrations.

---

# Частые ошибки

## Нет known good version

Нужно знать, какая версия была рабочей.

## Откатили app, но не config

Новая config может быть несовместима со старым кодом.

## Rollback не проверяли

Rollback runbook должен быть протестирован.

---

# Связанные заметки

- [[Continuous Delivery]]
- [[Deployment Strategies]]
- [[Helm]]
- [[GitOps]]
- [[Database Migrations]]
- [[Incident Response Flow]]

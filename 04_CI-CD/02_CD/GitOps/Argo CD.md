# Argo CD

`Argo CD` — GitOps/CD инструмент для Kubernetes.

Он читает desired state из Git/Helm/Kustomize и синхронизирует Kubernetes cluster с этим состоянием.

Argo CD относится к [[GitOps]] внутри [[Continuous Delivery]].

---

# Основная сущность

Главная сущность Argo CD — `Application`.

Application описывает:

```text
source repo/chart
path или chart
target revision
destination cluster/namespace
sync policy
health/sync status
```

То есть Application отвечает на вопрос:

```text
что откуда взять и куда применить
```

---

# Sync status и health

Sync status:

```text
Synced     actual state совпадает с desired state
OutOfSync  есть отличие
Unknown    Argo CD не смог сравнить
```

Health:

```text
Healthy
Progressing
Degraded
Suspended
Missing
Unknown
```

Важно: `Synced` не всегда значит `Healthy`.

Manifest может быть применён, но Pod всё ещё CrashLoopBackOff.

---

# Manual и auto sync

Manual sync:

```text
оператор нажимает sync или запускает argocd app sync
```

Auto sync:

```text
Argo CD сам применяет изменения из Git
```

Auto sync часто используют с дополнительными правилами:

```text
self-heal
prune
sync windows
approvals через Git process
```

---

# Команды

Login:

```bash
argocd login argocd.example.com
```

Список apps:

```bash
argocd app list
```

Статус:

```bash
argocd app get app-name
```

Sync:

```bash
argocd app sync app-name
```

Diff:

```bash
argocd app diff app-name
```

Через kubectl:

```bash
kubectl get applications -A
kubectl describe application app-name -n argocd
```

---

# App of Apps

App of Apps — паттерн, где одна root Application управляет другими Applications.

Полезно для bootstrap большого cluster.

Риск: если root app сломана, можно затронуть много приложений сразу.

---

# Argo CD vs FluxCD

Argo CD часто выбирают за:

```text
сильный UI
удобный diff
Application model
видимость для команд разработки
```

FluxCD часто выбирают за:

```text
toolkit/controllers approach
хорошую image automation
GitOps через CRD-first модель
меньше акцент на UI
```

Оба инструмента нормальные. Выбор зависит от команды и процесса.

---

# Частые проблемы

## OutOfSync

Desired state отличается от actual.

Проверить diff:

```bash
argocd app diff app-name
```

---

## Degraded

Manifest применён, но ресурс нездоров.

Смотреть Kubernetes:

```bash
kubectl get pods -n namespace
kubectl describe deploy app -n namespace
kubectl get events -n namespace --sort-by=.lastTimestamp
```

---

## Permission denied

Argo CD service account не имеет RBAC на нужные resources/namespaces.

---

# Связанные заметки

- [[GitOps]]
- [[Continuous Delivery]]
- [[Kubernetes]]
- [[Helm]]
- [[Kustomize]]
- [[RBAC]]

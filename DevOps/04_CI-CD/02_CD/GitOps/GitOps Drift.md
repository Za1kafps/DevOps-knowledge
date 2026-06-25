# GitOps Drift

`Drift` — ситуация, когда actual state окружения отличается от desired state в Git.

Пример:

```text
в Git replicas: 3
в cluster replicas: 5
```

GitOps controller видит отличие и может показать его или автоматически исправить.

---

# Откуда берётся drift

Частые причины:

```text
ручной kubectl edit
hotfix напрямую в cluster
controller/operator изменил resource
mutating admission webhook добавил поля
autoscaler изменил replicas
Helm chart генерирует нестабильные значения
```

Не каждый drift плохой. Например HPA легитимно меняет replicas.

Важно понимать, какие поля должны принадлежать Git, а какие runtime controllers.

---

# Почему drift опасен

Drift ломает воспроизводимость.

Если production руками поправили, а Git не обновили:

```text
новый cluster не поднимется так же
после reconcile hotfix исчезнет
incident повторится
audit trail неполный
```

---

# FluxCD

Проверить:

```bash
flux get all -A
flux diff kustomization app -n flux-system
```

Reconcile:

```bash
flux reconcile kustomization app -n flux-system --with-source
```

---

# Argo CD

Проверить:

```bash
argocd app get app-name
argocd app diff app-name
```

Sync:

```bash
argocd app sync app-name
```

---

# Как правильно чинить

Если изменение должно остаться:

```text
внести изменение в Git
review
merge
дать controller применить
```

Если изменение случайное:

```text
reconcile/sync из Git
проверить, кто сделал ручное изменение
закрыть доступ или процесс
```

---

# Частые ловушки

## GitOps возвращает hotfix назад

Hotfix сделали через `kubectl`, но не перенесли в Git.

## Controller постоянно меняет поле туда-сюда

Возможно, есть конфликт ownership с другим controller.

## Ignore differences скрывает реальную проблему

Ignore rules нужны точечно, а не чтобы “сделать зелёным”.

---

# Связанные заметки

- [[GitOps]]
- [[FluxCD]]
- [[Argo CD]]
- [[Kustomization]]
- [[HelmRelease]]

# API Server

`kube-apiserver` — центральная точка Kubernetes API.

Все изменения в cluster проходят через API Server:

```text
kubectl apply
controller reconcile
scheduler binding
kubelet status update
operator CRD update
```

---

# Что делает API Server

```text
принимает HTTPS requests
аутентифицирует клиента
проверяет authorization через RBAC
запускает admission chain
валидирует object schema
пишет состояние в etcd
отдаёт watch/list/get clients
```

---

# Request path

```text
client
  -> authentication
  -> authorization
  -> admission
  -> validation
  -> etcd
```

Если `kubectl` получает `Forbidden`, это RBAC.

Если `Unauthorized`, это authentication.

Если `admission webhook timeout`, запрос может зависнуть или упасть до записи в etcd.

---

# Проверка доступности

```bash
kubectl cluster-info
kubectl get --raw='/readyz?verbose'
kubectl get --raw='/livez?verbose'
kubectl get --raw='/version'
```

Проверка прав:

```bash
kubectl auth can-i create pods -n default
kubectl auth can-i '*' '*' --all-namespaces
```

---

# Частые проблемы

## Forbidden

Пользователь или ServiceAccount не имеет прав.

Смотри [[RBAC]].

---

## Webhook timeout

Admission webhook недоступен, а failurePolicy блокирует запрос.

Проверить:

```bash
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations
```

---

## API latency

Причины:

```text
etcd latency
слишком много watches
тяжёлые list requests
webhook latency
API Priority and Fairness throttling
```

---

# Связанные заметки

- [[Kubernetes Architecture]]
- [[etcd]]
- [[RBAC]]
- [[ServiceAccount]]
- [[Kubernetes Events]]

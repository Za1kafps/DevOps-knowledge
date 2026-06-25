# Sealed Secrets

`Sealed Secrets` — способ хранить Kubernetes Secrets в Git в зашифрованном виде.

Обычный Kubernetes Secret — это base64, не encryption.

SealedSecret шифруется публичным ключом controller, а расшифровать его может только controller в cluster.

---

# Как работает

```text
kubeseal берёт Secret
шифрует публичным ключом cluster
получается SealedSecret
SealedSecret хранится в Git
controller в cluster создаёт обычный Secret
```

---

# Пример

Создать Secret yaml:

```bash
kubectl create secret generic app-secret \
  --from-literal=password='secret' \
  --dry-run=client -o yaml > secret.yaml
```

Запечатать:

```bash
kubeseal -o yaml < secret.yaml > sealed-secret.yaml
```

Применить уже SealedSecret:

```bash
kubectl apply -f sealed-secret.yaml
```

---

# Важные ограничения

SealedSecret обычно привязан к:

```text
cluster key
namespace
secret name
scope
```

Если сменить namespace/name или cluster key, старый SealedSecret может не расшифроваться.

---

# SOPS vs Sealed Secrets

SOPS:

```text
гибкие backend keys
удобен для разных форматов
хорош для GitOps repo
```

Sealed Secrets:

```text
Kubernetes-focused
простая модель public key -> cluster decrypts
удобно для Secret manifests
```

Выбор зависит от процесса и того, где хранятся ключи.

---

# Частые проблемы

## SealedSecret не создаёт Secret

Проверить controller:

```bash
kubectl get pods -n kube-system | grep sealed
kubectl describe sealedsecret name -n namespace
```

## Wrong namespace/name

Secret был sealed для другого namespace или имени.

## Потерян private key controller

Старые SealedSecrets нельзя расшифровать.

Нужен backup ключа.

---

# Связанные заметки

- [[GitOps]]
- [[SOPS]]
- [[Secrets]]
- [[Secrets Management]]

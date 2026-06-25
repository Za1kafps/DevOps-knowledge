# SOPS

`SOPS` — инструмент для шифрования secrets в Git.

В GitOps он позволяет хранить encrypted YAML/JSON/env files, которые controller расшифровывает перед применением.

SOPS не делает secret безопасным сам по себе: безопасность зависит от ключей, access control и процесса review.

---

# Как работает

Файл содержит encrypted values и metadata о ключах.

Ключи могут быть:

```text
age
PGP
AWS KMS
GCP KMS
Azure Key Vault
HashiCorp Vault
```

В Git лежит encrypted content.

Cluster/controller должен иметь право расшифровать.

---

# Пример команд

Создать secret file:

```bash
sops secret.yaml
```

Расшифровать в stdout:

```bash
sops -d secret.yaml
```

Зашифровать существующий файл:

```bash
sops -e -i secret.yaml
```

---

# SOPS с FluxCD

Flux умеет decrypt SOPS secrets при reconcile, если настроены ключи.

Обычно:

```text
age private key хранится в Kubernetes Secret
Flux kustomize-controller использует decryption
encrypted secrets лежат в Git
```

---

# Что важно

```text
не коммитить decrypted files
разделять ключи dev/stage/prod
ограничивать доступ к private keys
иметь процедуру rotation
не шифровать огромные generated blobs без причины
```

---

# Частые проблемы

## Controller не может decrypt

Нет ключа или не тот key id.

## Человек закоммитил plaintext

Нужны pre-commit checks и secret scanning.

## Один ключ на все окружения

Компрометация dev даёт доступ к prod secrets.

---

# Связанные заметки

- [[GitOps]]
- [[FluxCD]]
- [[Sealed Secrets]]
- [[Secrets Management]]
- [[Supply Chain Security]]

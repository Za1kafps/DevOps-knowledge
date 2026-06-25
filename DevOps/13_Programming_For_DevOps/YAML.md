# YAML

YAML — формат сериализации, который часто используется Kubernetes, Ansible, CI и observability-конфигурациями. Отступы и типизация влияют на данные, поэтому файл нужно не только форматировать, но и валидировать схемой конкретного инструмента.

## Структуры

```yaml
service:
  name: api
  ports:
    - name: http
      port: 8080
  labels:
    tier: backend
  enabled: true
```

- mapping — пары key/value;
- sequence — список;
- scalar — строка, число, boolean или null.

TAB для indentation использовать нельзя.

## Строки

```yaml
plain: api
quoted: "true"
literal: |
  line one
  line two
folded: >
  this becomes
  one line
```

Если значение похоже на boolean, число, дату, wildcard или содержит специальные символы, безопаснее явно заключить его в кавычки.

## Anchors

```yaml
defaults: &defaults
  timeout: 10
  retries: 3

production:
  <<: *defaults
  retries: 5
```

Anchors относятся к YAML parser, но merge key поддерживается не всеми consumers одинаково. Kubernetes manifests обычно лучше собирать Helm/Kustomize, а не сложной системой anchors.

## Kubernetes

```bash
kubectl apply --dry-run=server -f manifest.yaml
kubectl diff -f manifest.yaml
kubeconform -strict manifest.yaml
```

`yamllint` проверяет YAML syntax/style, но не понимает Kubernetes schema. `kubectl --dry-run=server` также учитывает CRD и admission webhooks доступного cluster.

## CI

```bash
yamllint .
yq eval '.service.ports[] | select(.name == "http")' config.yaml
```

Не редактируй YAML через `sed`, если меняется структура: комментарий, multi-line scalar или одинаковый key могут привести к неверной замене. Используй parser (`yq`, Python library) или template engine.

## Безопасность

YAML может поддерживать object tags конкретного языка. Для недоверенных данных используй safe loader:

```python
yaml.safe_load(stream)
```

Секрет в YAML остаётся секретом только по названию. Base64 в Kubernetes Secret не является шифрованием.

## Типовые ошибки

- неправильный indentation;
- duplicate key незаметно перезаписан parser;
- `"false"` передан вместо boolean `false`;
- число/дата автоматически преобразованы неожиданным образом;
- multi-document файл разделён неверно;
- manifest синтаксически корректен, но не соответствует schema;
- secret попал в repository.

## Связи

- [[Programming for DevOps]]
- [[JSON]]
- [[Kubernetes]]
- [[Ansible]]
- [[GitLab CI]]
- [[Secrets]]

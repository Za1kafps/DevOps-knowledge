# Terraform

`Terraform` — инструмент Infrastructure as Code.

Он описывает desired state инфраструктуры в `.tf` файлах, сравнивает его с state и строит plan изменений.

---

# Главные понятия

```text
provider   API облака/сервиса
resource   объект инфраструктуры
data       чтение существующего объекта
state      текущее известное Terraform состояние
plan       diff между config и state/real world
apply      применение изменений
module     переиспользуемый набор ресурсов
```

---

# Workflow

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Для production:

```bash
terraform plan -out=tfplan
terraform apply tfplan
```

Так apply применяет именно просмотренный plan.

---

# State

State — критичный файл.

В нём могут быть:

```text
resource IDs
attributes
outputs
иногда sensitive values
```

Production state должен быть remote:

```text
S3 + locking
Terraform Cloud
GitLab managed state
cloud backend
```

Локальный `terraform.tfstate` нельзя терять и нельзя коммитить.

---

# Drift

Drift — реальная инфраструктура отличается от state/config.

Проверить:

```bash
terraform plan
```

Если кто-то поменял security group руками, Terraform может попытаться вернуть как в коде.

---

# Modules

Modules нужны для повторяемых блоков:

```text
vpc
service account
kubernetes cluster
database
monitoring stack
```

Не надо делать module на 3 строки только ради module.

---

# Частые ошибки

## apply без просмотра plan

Можно удалить/заменить production ресурс.

## state без locking

Два apply одновременно ломают state.

## secrets в state

Sensitive output скрывается в CLI, но может остаться в state.

## count/index для важных ресурсов

Удаление элемента из середины списка может пересоздать не то. Часто лучше `for_each`.

---

# Связанные заметки

- [[Infrastructure]]
- [[S3 Object Storage]]
- [[Vault]]
- [[CI-CD]]
- [[GitOps Drift]]

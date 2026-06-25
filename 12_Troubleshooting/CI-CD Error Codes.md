# CI-CD Error Codes

CI/CD ошибки надо читать по stage: checkout, deps, test, build, push, deploy.

---

# Частые классы

```text
exit code 1      команда завершилась ошибкой
exit code 127    command not found
exit code 137    killed, часто memory
permission denied
authentication failed
runner stuck
artifact not found
manifest unknown
```

---

# Проверка

```text
какой job/stage упал
какая команда последняя
изменились ли secrets/variables
доступен ли runner
есть ли artifact/cache
```

---

# Docker build в CI

```text
registry login
base image pull
Dockerfile path
build context
DinD/BuildKit/Kaniko права
```

---

# Связанные заметки

- [[CI-CD]]
- [[GitLab CI]]
- [[GitHub Actions]]
- [[Docker Build Failed]]

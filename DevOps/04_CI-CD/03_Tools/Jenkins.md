# Jenkins

`Jenkins` — extensible CI/CD сервер с pipelines, agents и большим plugin ecosystem.

Jenkins часто встречается в legacy и enterprise, где много кастомной automation.

---

# Основные части

```text
controller
agents
jobs
Jenkinsfile
plugins
credentials store
shared libraries
```

---

# Pipeline пример

```groovy
pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'go test ./...'
      }
    }
    stage('build') {
      steps {
        sh 'docker build -t app:${GIT_COMMIT} .'
      }
    }
  }
}
```

---

# Что важно поддерживать

```text
plugin updates
credentials hygiene
agent isolation
backup Jenkins home
shared libraries review
RBAC
audit
```

---

# Частые проблемы

## Plugin hell

Плагины конфликтуют или требуют обновления Jenkins core.

## Snowflake jobs

Jobs настроены через UI и не версионируются.

Лучше Jenkinsfile в Git.

## Agents загрязняются

Workspace/cache между builds может влиять на результат.

---

# Связанные заметки

- [[CI-CD]]
- [[Continuous Integration]]
- [[Secrets in CI-CD]]
- [[Artifacts and Cache]]

# SAST

`SAST` — Static Application Security Testing.

Это статический анализ кода на security-проблемы без запуска приложения.

SAST относится к [[Continuous Integration]] и [[Security]].

---

# Что ищет SAST

Примеры:

```text
SQL injection patterns
command injection
path traversal
hardcoded secrets
unsafe crypto
insecure deserialization
SSRF patterns
```

SAST не понимает весь runtime context, поэтому возможны false positives и false negatives.

---

# Где запускать

Обычно:

```text
merge request
main branch
scheduled scans
release pipeline
```

Для merge request важно показывать только новые findings или приоритетные проблемы, иначе разработчики перестают смотреть.

---

# Инструменты

Примеры:

```text
Semgrep
CodeQL
GitLab SAST
SonarQube
Gosec
Bandit
Brakeman
```

Выбор зависит от языка и процесса.

---

# Что делать с findings

Нужен triage:

```text
true positive
false positive
accepted risk
needs fix before merge
```

Без triage SAST превращается в отчёт, который никто не читает.

---

# Частые ошибки

## Скан есть, gate нет

Pipeline всегда зелёный, даже на critical finding.

## Gate слишком жёсткий сразу

Legacy проект может утонуть в старых findings.

Практичный подход: блокировать новые critical/high, старый backlog разгребать отдельно.

## Secrets ищут только SAST

Нужен отдельный secret scanning.

---

# Связанные заметки

- [[Continuous Integration]]
- [[Security]]
- [[Supply Chain Security]]
- [[Secrets in CI-CD]]

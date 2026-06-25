# Docker container exits immediately

Контейнер завершился сразу после старта.

Это обычно значит, что основной process внутри container завершился.

---

# Проверка

```bash
docker ps -a
docker logs <container>
docker inspect <container> --format '{{.State.ExitCode}}'
docker inspect <container> --format '{{.Config.Cmd}} {{.Config.Entrypoint}}'
```

---

# Частые причины

```text
приложение завершилось с ошибкой
неверный ENTRYPOINT/CMD
нет env/config
permission denied
порт занят не причина exit, но app может падать
команда одноразовая и успешно завершилась
```

---

# Debug

Запустить shell:

```bash
docker run --rm -it --entrypoint sh image
```

Если image distroless, нужен debug variant.

---

# Связанные заметки

- [[Docker]]
- [[Dockerfile]]
- [[Distroless Images]]

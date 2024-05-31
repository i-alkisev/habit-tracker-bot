## Совместный проект “Телеграм бот для отслеживания привычек”

Телеграм бот, который позволяет:
- добавлять для отслеживания пользовательские привычки
- отправлять напоминания
- сохранять и просматривать статистику выполнения

Требования к проекту
http://uneex.ru/LecturesCMC/PythonDevelopment2024/GraduateProject

## Doit команды
`doit html` - генерация документации

`doit localization` - генерация файлов для локализации

`doit style` - проверка стиля

`doit test` - запуск тестов

`doit erase` - удаление всех генератов

`doit run_bot` - запуск бота

## До запуска бота нужно

Добавить файл `db/db_secrets/db_password.txt` с паролем для базы данных

Создать файл set_credentials.sh:
```bash
#!/bin/bash

export DB_NAME="..."
export DB_USER="..."
export DB_PASS="..."
export DB_HOST="..."
export DB_PORT="..."
export BOT_TOKEN="..."
```

Далее выполнить:
```bash
chmod +x set_credentials.sh && . ./set_credentials.sh
```

## Pre-commit hooks

Для проверки стиля оформления кода и документации перед коммитом использованы flake8 и pydocstyle

```bash
pre-commit install
pre-commit run --all-files
```

## Локализация
Создать файл po/en_US.UTF-8/LC_MESSAGES/all.mo
```bash
pybabel compile -D all -l en_US.UTF-8 -d po -i po/en_US.UTF-8/LC_MESSAGES/all.po
```
Для выбора русского языка:
```bash
export LC_CTYPE=ru_RU.UTF-8
```
Для выбора английского языка:
```bash
export LC_CTYPE=en_US.UTF-8
```

## Документация
```bash
cd docs
make html
```
Открываем docs/_build/html/index.html 

Аналогично для user_docs

## ToDo
- [ ] поправить начальное состояние (при перезапуске бота, первая команда (если это не /start) не распознается)
- [ ] добавить всевозможные проверки для данных, получаемых от пользователя
- [ ] добавить логирование в обработке ошибок (см. notifier.py)

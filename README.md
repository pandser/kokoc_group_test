# kokoc_group_test

## Тестовое задание на позицию Python-разработчик в Kokoc Group

### Задача: 
Ваша задача написать Django-приложение, которое будет отображать курс
валюты по отношению к рублю на заданную дату. При обращении к приложению по
адресу http://localhost:8000/rate/?charcode=AUD&date=2024-01-01 , оно должно выводить
результат в виде JSON в формате:
```
{
"charcode": "AUD",
"date": "2024-01-01",
"rate": 57.0627
}
```
Данные по валютам должны храниться в базе данных приложения.
А для пополнения этой базы данных нужно написать команду, которая
будет раз в сутки обращаться к сервису ЦБ за актуальными курсами валют по адресу:
https://www.cbr-xml-daily.ru/daily_json.js

### Запуск проекта в dev-режиме:

Клонировать репозиторий и перейти в него в командной строке:

```bash
    git clone <ссылка с git-hub>
```

Cоздать виртуальное окружение:

```bash
    python3 -m venv venv
```

Активируйте виртуальное окружение

```bash
    source venv/bin/activate
```

Установите зависимости из файла requirements.txt

```bash
    pip install -r requirements.txt
```

Сделать миграции:

```
    python manage.py migrate
```

Создать суперюзера:

```
    python manage.py createsuperuser
```

В папке с файлом manage.py выполните команду:

```bash
    python manage.py runserver
```

Команда для получения данных из ЦБ:

```bash
    python manage.py getdailyrate
```

crontab:
```
   @daily cd ~/<путь к папке с проектом> && source venv/bin/activate && python manage.py getdailyrate 
```


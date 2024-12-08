# YaCut

## Технологии:

- Python 3.9.13
- Flask 3.0.2
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.5
- Flask-WTF 1.2.1

## Установка (Windows):

1. Клонирование репозитория

```
git clone https://github.com/Sergey-Tsepilov/yacut.git
```

2. Переход в директорию yacut

```
cd yacut
```

3. Создание виртуального окружения

```
python -m venv venv
```

4. Активация виртуального окружения

```
source venv/Scripts/activate
```

5. Обновите pip

```
python -m pip install --upgrade pip
```

6. Установка зависимостей

```
pip install -r requirements.txt
```

7. Создание и настройка базы данных

```
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```

Теперь примените миграции для настройки базы данных:

```
flask db upgrade
```

8. Запуск приложения

```
flask run
```

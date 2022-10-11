# api_yamdb
# Пример реализации API на базе Django REST Framework

Позволяет работать с моделями базы:
- User (Пользователи)

# Установка:
### -настройте виртуальное окружение

    source venv/bin/activate

### -установите необходимые зависимости

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

### -разверните базу данных

    python3 manage.py makemigrations
    python3 manage.py migrate

### - запустите проект

    python manage.py runserver


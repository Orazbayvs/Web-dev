#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# # 1. Активировать виртуальное окружение
# source venv/bin/activate

# # 2. Применить миграции
# python manage.py makemigrations
# python manage.py migrate

# # 3. Создать суперпользователя для админки
# python manage.py createsuperuser

# # 4. Запустить сервер
# python manage.py runserver
# http://127.0.0.1:8000/api/products/
# http://127.0.0.1:8000/api/categories/
run:
    autopep8 -v --global-config autopep8.toml .
    python manage.py runserver 0.0.0.0:8000

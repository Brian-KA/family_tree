release: python manage.py migrate --noinput && python manage.py createsuperuser --noinput
web: gunicorn family.wsgi
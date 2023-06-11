release: python manage.py migrate && && DJANGO_SUPERUSER_PASSWORD=chasin@98! python manage.py createsuperuser --noinput --username=admin
web: gunicorn family.wsgi
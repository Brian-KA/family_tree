# family tree setup
## activate venv
` bin/activate ` # for windows

## install dependencies
` pip install -r requirements.txt `

## static and media files configurations
> settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
```
> url.py
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## create superuser
` python manage.py createsuperuser `

## create migrations
` python manage.py makemigrations `

## migrate
` python manage.py migrate `

## run the app
` python manage.py runserver `
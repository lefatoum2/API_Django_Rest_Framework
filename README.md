
## Environnement virtual

```
pip install pipenv
pipenv shell
```

## Installation des packages
```
pip install django
pip install djangorestframework
```

## Création du projet 
```
 django-admin startproject Newspaper
 python manage.py startapp main
```


settings.py : 
```py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main', 
    'rest_framework'
]
```
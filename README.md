
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

## Model

```py
from django.db import models
# Create your models here.
class Todo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)
def __str__(self):
        return self.Title
```
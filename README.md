
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

models.py :

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

serializers.py :

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'Title', 'Description', 'Date')
```

```
python manage.py makemigrations
python manage.py migrate
```
## Les vues
views.py : 

```py
from rest_framework import generics
from .serializers import *
from .models import *

class ListArticle(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class DetailArticle(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class CreateArticle(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class DeleteArticle(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

## URLS

main/urls.py :

```py
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', DetailArticle.as_view()),
    path('', ListArticle.as_view()),
    path('create', CreateArticle.as_view()),
    path('delete/<int:pk>', DeleteArticle.as_view())
]

```

### Lancement

```
py manage.py runserver
```
# API avec DJANGO REST FRAMEWORK

![img6](./img/rest.jpg)]


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

## Models

models.py :

```py
from django.db import models
# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    
def __str__(self):
        return self.Title
```

serializers.py :

```py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
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
http://127.0.0.1:8000/api
![img6](./img/rest2.jpg)]

http://127.0.0.1:8000/api/create
![img6](./img/rest1.jpg)]
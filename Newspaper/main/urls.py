from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', DetailArticle.as_view()),
    path('', ListArticle.as_view()),
    path('create', CreateArticle.as_view()),
    path('delete/<int:pk>', DeleteArticle.as_view())
]
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
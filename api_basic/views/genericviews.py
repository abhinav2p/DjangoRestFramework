from rest_framework import generics
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer


class GenericArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class GenericArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

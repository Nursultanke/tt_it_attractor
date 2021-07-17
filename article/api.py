from rest_framework.generics import (ListAPIView)
from article.serializers import *


class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='main'),
    path('article_detail/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article_add', views.CreateArticle.as_view(), name='article_add'),
    path('article_update/<int:pk>', views.UpdateArticle.as_view(), name='article_update'),
    path('article_delete/<int:pk>', views.delete_article, name='article_delete'),
    path('category_list', views.CategoryView.as_view(), name='category_list'),
    path('category_create', views.CreateCategory.as_view(), name='category_create'),
    path('category_update/<int:pk>', views.UpdateCategory.as_view(), name='category_update'),
    path('category_delete/<int:pk>', views.category_delete, name='category_delete'),
]

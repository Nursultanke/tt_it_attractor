from django.db import models
from django.conf import settings
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    parent_id = models.ForeignKey('self', verbose_name='Категория', on_delete=models.CASCADE)


class Article(models.Model):
    category_id = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Картинки')

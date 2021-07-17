from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from article.forms import IncomeDebitsForm
from article.models import *
from users.models import User


class ArticleView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login'
    model = Article
    template_name = 'pages/main.html'


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    model = Article
    template_name = 'pages/article_detail.html'


class CreateArticle(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login'
    model = Article
    fields = ('category_id', 'title', 'description', 'image')
    template_name = 'pages/article_create_update.html'

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.request.user)
        form.instance.user = user

        return super(CreateArticle, self).form_valid(form)


class UpdateArticle(LoginRequiredMixin, generic.UpdateView):
    login_url = '/accounts/login'
    model = Article
    fields = ('category_id', 'title', 'description', 'image')
    template_name = 'pages/article_create_update.html'

    success_url = '/'


@login_required
def delete_article(request, pk):
    get_object_or_404(Article, pk=pk).delete()
    return redirect('main')


class CategoryView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login'
    model = Category
    template_name = 'pages/category_list.html'


class CreateCategory(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login'
    model = Category
    fields = '__all__'
    template_name = 'pages/category_create_update.html'
    success_url = '/category_list'


class UpdateCategory(LoginRequiredMixin, generic.UpdateView):
    login_url = '/accounts/login'
    model = Category
    fields = '__all__'
    template_name = 'pages/category_create_update.html'
    success_url = '/category_list'


@login_required
def category_delete(request, pk):

    get_object_or_404(Category, pk=pk).delete()
    return redirect('category_list')
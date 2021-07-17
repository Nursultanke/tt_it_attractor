from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from article.views import ArticleView
from users.forms import CustomUserRegisterForm
from users.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Это имя уже занята')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Эта почта уже занята')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Вы зарегистрированы и можете войти в свой аккаунт')
                    return redirect('login')
        else:
            messages.error(request, 'Пароль не совпадает')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Не верное имя или пароль')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('login')


class UserList(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login'
    model = User
    template_name = 'pages/user_list.html'


class UserUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/accounts/login'
    model = User
    fields = ('username',)
    template_name = 'pages/user_create_update.html'
    success_url = '/accounts/user_list'


class UserCreate(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login'
    user_add_form = CustomUserRegisterForm
    template_name = 'pages/user_create_update.html'

    def get(self, request, *args, **kwargs):
        form = self.user_add_form()
        context = {'form': form, }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.user_add_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            return redirect('user_list')
        context = {'form': form}
        return render(request, self.template_name, context)


class UserPasswordChange(LoginRequiredMixin, PasswordChangeView):
    login_url = '/accounts/login'
    form_class = PasswordChangeForm
    template_name = 'pages/user_password_change.html'
    success_url = '/'


@login_required
def user_delete(request, pk):
    if request.user.is_authenticated:
        get_object_or_404(User, pk=pk).delete()
    return redirect('user_list')

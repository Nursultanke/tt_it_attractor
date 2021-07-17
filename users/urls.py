from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('exit', views.logout, name='logout'),
    path('user_list', views.UserList.as_view(), name='user_list'),
    path('user_create', views.UserCreate.as_view(), name='user_create'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('user_password_change', views.UserPasswordChange.as_view(), name='user_password_change'),
    path('user_delete/<int:pk>', views.user_delete, name='user_delete'),

]


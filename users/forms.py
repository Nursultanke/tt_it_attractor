from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class SimpleUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ['username']
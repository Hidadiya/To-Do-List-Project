from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email',
        'password1','password2'
        )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']


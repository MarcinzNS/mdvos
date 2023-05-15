from django.contrib.auth.forms import UserCreationForm
from .models.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    username = forms.CharField(label='Nazwa użytkownika')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput,
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
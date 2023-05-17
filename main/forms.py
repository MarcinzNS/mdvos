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

    # nadpisanie error_messages
    error_messages = {
        "password_mismatch": "Hasła muszą być takie same",
    }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Podana nazwa użytkownika jest już zajęta.')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Podany adres email jest już zajęty.')

        if first_name and len(first_name) > 30:
            self.add_error('first_name', 'Imię przekracza maksymalną długość 30 znaków.')
        
        if last_name and len(last_name) > 30:
            self.add_error('last_name', 'Nazwisko przekracza maksymalną długość 30 znaków.')
        
        if username and len(username) > 50:
            self.add_error('username', 'Nazwa użytkownika przekracza maksymalną długość 50 znaków.')
          
        if password1 and len(password1) > 50:
            self.add_error('password1', 'Hasło przekracza maksymalną długość 50 znaków.')

        return cleaned_data
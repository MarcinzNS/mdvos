from django.contrib.auth.forms import UserCreationForm
from .models.models import User, Devices
from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name_max_len = 30
    last_name_max_len = 30
    username_max_len = 30
    email_max_len = 50

    first_name = forms.CharField(
        label='Imię',
        required=False,
        max_length=first_name_max_len,
        error_messages={
            'max_length': f"Imię nie może przekraczać {first_name_max_len} znaków",
        }
    )
    last_name = forms.CharField(
        label='Nazwisko',
        required=False,
        max_length=last_name_max_len,
        error_messages={
            'max_length': f"Nazwisko nie może przekraczać {last_name_max_len} znaków",
        }
    )
    
    username = forms.CharField(
        label='Nazwa użytkownika',
        max_length=30,
        error_messages={
            'required': "Należy wpisać nazwę użytkownika",
            'max_length': f"Nazwa użytkownika nie może przekraczać {username_max_len} znaków",
            "unique": f"Podana nazwa użytkownika jest już zajęta",
        }
    )

    email = forms.EmailField(
        label='Email',
        max_length=email_max_len,
        error_messages={
            'required': "Należy wpisać adres email",
            'max_length': f"Email nie może przekraczać {email_max_len} znaków",
            "unique": f"Konto o podanym adresie email już istnieje.",
        }
    )
    
    password1 = forms.CharField(
        label=("Hasło"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        error_messages={
            'required': "Należy wpisać hasło",
        }
    )
    
    password2 = forms.CharField(
        label=("Powtórz hasło"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        error_messages={
            'required': "Należy powtórzyć hasło"
        }
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    # nadpisanie error_messages
    error_messages = {
        "password_mismatch": "Hasła muszą być takie same",
    }


class AddDeviceForm(forms.ModelForm):
    brand = forms.CharField(
        label="Marka",
        max_length=30,
    )

    model = forms.CharField(
        label="Model",
        max_length=50,
    )

    device_type = forms.ChoiceField(
        label="Kategoria",
        choices=[
            ("PHONE", "Telefon"),
            ("TABLET", "Tablet"),
            ("LAPTOP", "Laptop"),
        ],
    )
    release_date = forms.DateField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Devices
        fields = ['brand', 'model', 'device_type', 'release_date', 'image']

    def save(self, commit=True):
        # zapisanie wartości release_date w premier
        instance = super().save(commit=False)
        instance.premier = self.cleaned_data['release_date']

        if commit:
            instance.save()
        return instance


class EditUserForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        required=False,
    )

    first_name = forms.CharField(
        label='Imię',
        required=False
    )
    last_name = forms.CharField(
        label='Nazwisko',
        required=False,
    )

    def save(self, commit=True):
        instance = super().save(commit=False)
    
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email'] 
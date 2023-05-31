from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ngettext
from django.utils.deconstruct import deconstructible

class MinimumLengthValidator:

    #Sprawdza czy hasło ma odpowiednią długość.

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    f"Hasło musi zawierać co najmniej {self.min_length} znaków.",
                    f"Hasło musi zawierać co najmniej {self.min_length} znaków.",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            f"Hasło musi zawierać co najmniej {self.min_length} znaków.",
            f"Hasło musi zawierać co najmniej {self.min_length} znaków.",
            self.min_length,
        )
    

@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = f"Nazwa użytkownika może zawierać tylko litery, cyfry oraz znaki @ . + - _"
    flags = 0
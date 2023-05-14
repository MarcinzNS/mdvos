from django.contrib.auth.models import User

def correctnessOfLoginData(email, password):
    data = User.objects.all().filter(email=email, password=password).values()[0]
    print("DATA:", data)
    return len(data.keys()) > 0
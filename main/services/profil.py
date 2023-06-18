from main.models.models import User
from django.contrib import messages

def profil_save_edit(request):
    user = request.user
    if len(request.POST['first_name']):
            user.first_name = request.POST['first_name']
            user.save()

    if len(request.POST['last_name']):
        user.last_name = request.POST['last_name']
        user.save()

    if len(request.POST['username']):
        new_username = request.POST['username']

        if User.objects.filter(username=new_username).exists():
            messages.error(request, "Nazwa użytkownika już istnieje")
        else:
            user.username = new_username
            user.save()

    if len(request.POST['email']):
        new_email = request.POST['email']

        if User.objects.filter(email=new_email).exists():
            pass
        else:
            user.email = new_email  
            user.save()
    return True

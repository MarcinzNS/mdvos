from main.models.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

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

def profil_save_password_change(request):
    user = request.user
    old_password = request.POST['old_password']
    if request.user.check_password(old_password):

        new_password1 = request.POST['password1']
        new_password2 = request.POST['password2']
        if new_password1 == new_password2:
            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Twoje hasło zostało zmienione.')
            return redirect('profile')
        else:
            messages.error(request, 'Podane hasła nie są identyczne.')
            return redirect('profile')
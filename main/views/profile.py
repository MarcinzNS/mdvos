from django.shortcuts import render, redirect
import datetime
from ..forms import EditUserForm
from main.models.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

def profile(request):
    if not request.user.is_authenticated:
        request.session['next_page'] = request.get_full_path()
        return redirect('login')
    
    form = EditUserForm()
    context = {
        'form': form,
    }

    if request.method == "POST":       
        if "save_password_change" in request.POST:
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                new_password1 = form.cleaned_data['password1']
                new_password2 = form.cleaned_data['password2']
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Twoje hasło zostało zmienione.')
                    return redirect('profile')
                else:
                    messages.error(request, 'Podane hasła nie są identyczne.')

        elif "save_edit" in request.POST:
            user = request.user

            # nie działają polskie znaki
            
            if len(request.POST['first_name']):
                user.first_name = request.POST['first_name']
            
            if len(request.POST['last_name']):
                user.last_name = request.POST['last_name']
            
            if len(request.POST['username']):
                new_username = request.POST['username']

                if User.objects.filter(username=new_username).exists():
                    messages.error(request, "Nazwa użytkownika już istnieje")
                else:
                    user.username = new_username

            if len(request.POST['email']):
                new_email = request.POST['email']

                if User.objects.filter(email=new_email).exists():
                    pass
                else:
                    user.email = new_email   

            user.save()
            

    return render(request, "profile.html", context)




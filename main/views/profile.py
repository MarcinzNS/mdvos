# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
import datetime
from ..forms import EditUserForm
from ..services.profil import profil_save_edit
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import chardet

def profile(request):
    if not request.user.is_authenticated:
        request.session['next_page'] = request.get_full_path()
        return redirect('login')

    form = EditUserForm()
    context = {'form': form}

    if request.method == "POST":       
        if "save_password_change" in request.POST:
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


        elif "save_edit" in request.POST:
            profil_save_edit(request)

    return render(request, "profile.html", context)




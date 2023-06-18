# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
import datetime
from ..forms import EditUserForm
from ..services.profil import profil_save_edit, profil_save_password_change
from django.contrib import messages

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
            profil_save_password_change(request)


        elif "save_edit" in request.POST:
            profil_save_edit(request)

    return render(request, "profile.html", context)




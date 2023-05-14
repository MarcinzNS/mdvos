from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..services.login_system import *
import datetime

# Create your views here.
def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if correctnessOfLoginData(email, password):
            return redirect("devices")
    return render(request, "login.html", context)

# Create your views here.
def registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        nick = request.POST["nick"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create()
        user.password = password
        user.username = nick
        user.email = email
        user.first_name = name
        user.last_name = surname
        user.save()

        messages.success(request, "Twoje konto zostało stworzone!")
        return redirect("registration")

    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "register.html", context)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

# Create your views here.
def login(request):
    context = {
        "now" : datetime.datetime.now()
    }
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
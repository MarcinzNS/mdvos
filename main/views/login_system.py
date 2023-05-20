from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate


def loginUser(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Błędne dane logowania")

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()

            # w tym momencie django samo jeszcze nie ogarnia że trzbea użyć EmailBackend
            user.backend = "main.services.authentication.EmailBackend"

            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'register.html', {'form': form})
        
    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
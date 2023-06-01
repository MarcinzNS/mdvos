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
        next_page = request.session.get('next_page')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if next_page:
                return redirect(next_page)
            else:
                return redirect('home')
        else:
            messages.error(request, "Błędne dane logowania")

    return render(request, "login.html", context)


def logoutUser(request):

    next_page = request.session.get('next_page')
    logout(request)

    if next_page:
        return redirect(next_page)
    else:
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

            messages.success(request, "Pomyślnie założono konto")
            return render(request, 'login.html', {'form': form})

        else:
            return render(request, 'register.html', {'form': form})
        
    form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
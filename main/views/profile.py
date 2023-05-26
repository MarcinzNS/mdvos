from django.shortcuts import render, redirect
import datetime

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        "now" : datetime.datetime.now(),
        "name" : 'Zdzichu',
        "surname" : 'Wieratara',
        "mail": 'przypadkowy@mail.com'
    }
    
    return render(request, "profile.html", context)
from django.shortcuts import render, redirect
import datetime

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "profile.html", context)
from django.shortcuts import render
import datetime

# Create your views here.
def login(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "index.html", context)

# Create your views here.
def registration(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "index.html", context)
from django.shortcuts import render
import datetime

# Create your views here.
def devices(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "index.html", context)

# Create your views here.
def one_device(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "index.html", context)
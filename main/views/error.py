from django.shortcuts import render
import datetime

# Create your views here.
def error(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "error404.html", context)
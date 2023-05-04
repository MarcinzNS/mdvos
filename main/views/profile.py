from django.shortcuts import render
import datetime

# Create your views here.
def profile(request):
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "index.html", context)
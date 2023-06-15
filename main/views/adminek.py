from django.shortcuts import render, redirect
import datetime

def adminek(request):
    if not request.user.is_staff:
        return redirect('error404')
    
    context = {
        "now" : datetime.datetime.now()
    }
    return render(request, "admin.html", context)
from django.shortcuts import render, redirect
import datetime
from ..forms import EditUserForm
from main.models.models import User

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = EditUserForm()
    context = {
        'form': form
    }

    if request.method == "POST":       
        if "save_password_change" in request.POST:
            pass

        elif "save_edit" in request.POST:
            user = request.user
            
            if len(request.POST['first_name']):
                user.first_name = request.POST['first_name']
            
            if len(request.POST['last_name']):
                user.last_name = request.POST['last_name']

            user.save()
            

    return render(request, "profile.html", context)




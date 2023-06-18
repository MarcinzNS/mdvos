from django.shortcuts import render, redirect
from ..forms import OSVersionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models.models import  OS_devices,Devices
from ..services.devices import *

@login_required(login_url='login')
def add_os(request):
    if request.method == "POST":
        os_version_form = OSVersionForm(request.POST, request.FILES ,devices=Devices.objects.all())
        if os_version_form.is_valid():
            ADD_OS(os_version_form)
            messages.success(request, "Dodano nowy system operacyjny.")
            return render(request, "add_os.html", {'os_version_form': os_version_form})
            
    else:
        os_version_form = OSVersionForm(devices=Devices.objects.all())

    return render(request, "add_os.html", {'os_version_form': os_version_form})


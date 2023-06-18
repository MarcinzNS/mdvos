from django.shortcuts import render, redirect
from ..forms import OSVersionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models.models import  OS_devices,Devices

@login_required(login_url='login')
def add_os(request):
    if request.method == "POST":
        os_version_form = OSVersionForm(request.POST, request.FILES ,devices=Devices.objects.all())
        if os_version_form.is_valid():
            os_version = os_version_form.save(commit=False)
            os_version.accepted = False
            os_version.save()
            os_version_form.save_m2m()

            devices = os_version_form.cleaned_data['devices']  # Pobranie zaznaczonych urządzeń
            for device in devices:
                OS_devices.objects.create(os_id=os_version, devices_id=device)

            messages.success(request, "Dodano nowy system operacyjny.")
            return render(request, "add_os.html", {'os_version_form': os_version_form})
            
    else:
        os_version_form = OSVersionForm(devices=Devices.objects.all())

    return render(request, "add_os.html", {'os_version_form': os_version_form})


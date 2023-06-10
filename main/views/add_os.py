from django.shortcuts import render, redirect
from ..forms import OSVersionForm, OSForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models.models import OS, OS_version, OS_devices,Devices

@login_required(login_url='login')
def add_os(request):
    if request.method == "POST":
        os_version_form = OSVersionForm(request.POST, devices=Devices.objects.all())
        if os_version_form.is_valid():
            os_version = os_version_form.save(commit=False)
            os_version.accepted = False
            os_version.save()
            os_version_form.save_m2m()

            devices = os_version_form.cleaned_data['devices']  # Pobranie zaznaczonych urządzeń
            for device in devices:
                OS_devices.objects.create(os_id=os_version, devices_id=device)

            messages.success(request, "Dodano nowy system operacyjny.")
            return redirect('add_os')
    else:
        os_version_form = OSVersionForm(devices=Devices.objects.all())

    return render(request, "add_os.html", {'os_version_form': os_version_form})

# def add_os(request):
#     if request.method == 'POST':
#         os_form = OSForm(request.POST)
#         os_version_form = OSVersionForm(request.POST)
#         if os_form.is_valid() and os_version_form.is_valid():
#             os = os_form.save()
#             os_version = os_version_form.save(commit=False)
#             os_version.os_id = os
#             os_version.save()
#             os_version_form.save_m2m()  # Zapisanie powiązań z urządzeniami
#             messages.success(request, "Dodano nowy system operacyjny.")
#             return redirect('add_os')
#     else:
#         os_form = OSForm()
#         os_version_form = OSVersionForm()

#     # Inicjalizacja pola devices w formularzu
#     os_version_form.fields['devices'].queryset = Devices.objects.all()

#     context = {
        
#         'os_version_form': os_version_form,
#     }
#     return render(request, 'add_os.html', context)

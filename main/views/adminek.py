from django.shortcuts import render, redirect
import datetime
from ..services.admin import *

def adminek(request):
    if not request.user.is_staff:
        return redirect('error404')
    
    context = {
        "now" : 1
    }
    return render(request, "admin.html", context)

def pomoc(request):
    if not request.user.is_staff:
        return redirect('error404')
    data = getUnaccepted()
    context = {
        "data" : data["data"]
    }
    return render(request, "pomoc.html", context)

def accept_device(request, device_id):
    if not request.user.is_staff:
        return redirect('error404')
    try:
        device = models.Devices.objects.get(id_device=device_id)
        device.accepted = True
        device.save()
        messages.success(request, 'Zaakceptowano produkt')
    except:
        messages.warning(request, 'Nie udało się zaakceptować produktu')

    
    return redirect('pomoc')

def remove_device_from_db(request, device_id):
    if not request.user.is_staff:
        return redirect('error404')

    try:
        device = models.Devices.objects.get(id_device=device_id)
        device.delete()
        messages.success(request, 'Pomyślnie usunięto produkt')

    except:
        messages.warning(request, 'Nie udało się usunąć produktu')
    
    return redirect('pomoc')



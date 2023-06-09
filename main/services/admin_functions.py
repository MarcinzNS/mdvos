from django.shortcuts import redirect
from main.models import models

def remove_device(request, device_id):
    
    if not request.user.is_staff:
        return redirect('devices')
    
    try:
        device = models.Devices.objects.get(id_device=device_id)
        device.accepted = False
        device.save()

    except:
        pass

    return redirect('devices')
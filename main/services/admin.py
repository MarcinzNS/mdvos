from ..models.models import Devices, Specification
from django.db.models import Q
from main.models.models import Devices
from django.shortcuts import get_object_or_404, redirect
from ..services.devices import *
from ..services.os import *
from django.contrib import messages
from main.models import models


def getUnaccepted():
    devices = Devices.objects.filter(accepted=False)
    devices = devices.values()

    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))
    result = []
    for device in devices:
        device_specifications = [spec for spec in specifications if spec['devices_id'] == device['id_device']]
        device_data = {
            'device': 
                device,
            'specifications': 
                {spec['spec_type_id__name']: spec['value'] for spec in device_specifications}
        }
        result.append(device_data)
    return {"data": result}


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


def edit_device_specs(specs_data, device_id):
    cpu = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='CPU'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    cpu.value = specs_data['cpu']
    cpu.save()

    ram = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='RAM'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    ram.value = specs_data['ram']
    ram.save()

    screen_size = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='SIZE'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    screen_size.value = specs_data['screen_size']
    screen_size.save()

    battery = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='BATTERY'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    battery.value = specs_data['battery']
    battery.save()

    disk = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='DISC'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    disk.value = specs_data['disk_size']
    disk.save()


def get_device(device_id):
    return models.Devices.objects.get(id_device=device_id)


def remove_device(device_id):
    device = models.Devices.objects.get(id_device=device_id)
    device.accepted = False
    device.save()
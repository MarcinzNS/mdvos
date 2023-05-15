from ..models.models import Devices, Specification
from django.db.models import Q

def getDevicesDataForPage(how_many, which_page):
    start = (which_page-1)*how_many
    devices_from_db = Devices.objects.all().order_by('name').values()
    devices = []
    for device in devices_from_db:
        devices.append(device | Specification.objects.all().filter(devices_id=device["id_device"]).values()[0])
    return {"data": devices[start:start+how_many], "how_many_results": len(devices)}

def getDevicesFiltredDataForPage(how_many, which_page, brand_filter, ram_filter):
    start = (which_page-1)*how_many
    devices_from_db = Devices.objects.all().order_by('name').values()
    devices = []
    for device in devices_from_db:
        spec = Specification.objects.all().filter(devices_id=device["id_device"]).values()[0]
        if device["name"] in brand_filter or spec["ram"] in ram_filter:
            devices.append(device | spec)
    return {"data": devices[start:start+how_many], "how_many_results": len(devices)}

def getDeviceData(id):
    return Devices.objects.all().filter(id_device=id).values()[0]

def getSpecificationData(id):
    return  Specification.objects.all().filter(devices_id=id).values()[0]

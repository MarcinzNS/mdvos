from ..models.models import Devices, Specification

def getDevicesDataForPage(how_many, which_page):
    start = (which_page-1)*how_many
    devices_from_db = Devices.objects.all().order_by('name').values()[start:start+how_many]
    devices = []
    for device in devices_from_db:
        devices.append(device | Specification.objects.all().filter(devices_id=device["id_device"]).values()[0])
    return devices

def getHowManyDevices():
    return len(Devices.objects.all())

def getDeviceData(id):
    devices = Devices.objects.all().filter(id_device=id).values()
    return devices

def getSpecificationData(id):
    specification = Specification.objects.all().filter(devices_id=id).values()
    return specification
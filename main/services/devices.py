from ..models.models import Devices

def getDevicesDataForPage(how_many, which_page):
    return Devices.objects.all().order_by('name').values()[which_page-1:which_page-1+how_many]

def getHowManyDevices():
    return len(Devices.objects.all())
from ..models.models import Devices

def getDevicesDataForPage(how_many, which_page):
    start = (which_page-1)*how_many
    return Devices.objects.all().order_by('name').values()[start:start+how_many]

def getHowManyDevices():
    return len(Devices.objects.all())
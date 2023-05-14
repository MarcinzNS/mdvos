from django.shortcuts import render
from ..services.devices import *
import math

def devices(request, page=1):
    how_many_item_on_page = 2
    context = {
        "data": 
            getDevicesDataForPage(how_many_item_on_page, page),
        "how_many_pages": 
            [i+1 for i in range(math.ceil(getHowManyDevices()/how_many_item_on_page))],
        "show_arrow": 
            [page >= 2, page+1 <= math.ceil(getHowManyDevices()/how_many_item_on_page)],
        "page": 
            {"previous": page-1, "next": page+1, "show_pages_controler": math.ceil(getHowManyDevices()/how_many_item_on_page) > 1}
    }
    return render(request, "devices.html", context)

def one_device(request, id):
    context = {
        "device" : getDeviceData(id),
        "specification" : getSpecificationData(id),
    }
    return render(request, "device.html", context)
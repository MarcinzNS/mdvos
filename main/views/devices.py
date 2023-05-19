from django.shortcuts import render
from ..services.devices import *
import math

def devices(request, category="NOT", how_many_item_on_page=2, page=1,):
    context = {
        "sidebar": {
            "brand": ["Xiaomi", "Samsung", "Apple", "Motorola"],
            "ram": [6, 8, 12, 16, 18],
        }
    } 
    brand_filter = []
    ram_filter = []
    urlEnd = ""
    if request.method == "GET":
        urlEnd = GETtoURL(request.GET)
        brand_filter = [brand_name for brand_name in context["sidebar"]["brand"] if request.GET.get(brand_name, False)]
        ram_filter = [ram_value for ram_value in context["sidebar"]["ram"] if request.GET.get(f"ram{ram_value}", False)]
        
    if len(brand_filter) + len(ram_filter) == 0:
        data = getDevicesDataForPage(category, how_many_item_on_page, page, [], [])
    else:
        data = getDevicesDataForPage(how_many_item_on_page, page, brand_filter, ram_filter)
    
    how_many_pages = math.ceil(data["how_many_results"]/how_many_item_on_page)
    context |= {
        "data": data["data"],
        "how_many_pages": [i+1 for i in range(how_many_pages)],
        "show_arrow": [page >= 2, page+1 <= how_many_pages],
        "page": {
            "previous": page-1,
            "next": page+1,
            "show_pages_controler": how_many_pages > 1
        },
        "how_many_item_on_page": how_many_item_on_page,
        "filters": {
            "brand": brand_filter, 
            "ram": ram_filter
        },
        "urlEnd": urlEnd
    }
    return render(request, "devices.html", context)

def GETtoURL(getDict):
    url = "?"
    for key in getDict:
        url += f"{key}={getDict[key]}&"
    return url[:-1]

def one_device(request, id):
    context = {
        "device" : getDeviceData(id),
        "specification" : getSpecificationData(id),
    }
    return render(request, "device.html", context)
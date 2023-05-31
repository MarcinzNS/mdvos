from django.shortcuts import render, get_object_or_404
from ..services.devices import *
from ..services.os import *

import math

def devices(request, category="NOT", sort_by="NOT", how_many_item_on_page=2, page=1,):
    context = {
        "sidebar": {
            "brand": ["Xiaomi", "Samsung", "Apple", "Motorola"],
            "ram": [6, 8, 12, 16, 18],
            "sort_by": {"Sortuj wg daty": "premier", "Sortuj po nazwie": "brand", "Sortuj po nazwie modelu": "model"}
        }
    } 
    brand_filter = []
    ram_filter = []
    urlEnd = ""
    if request.method == "GET":
        urlEnd = GETtoURL(request.GET)
        brand_filter = [brand_name for brand_name in context["sidebar"]["brand"] if request.GET.get(brand_name, False)]
        ram_filter = [ram_value for ram_value in context["sidebar"]["ram"] if request.GET.get(f"ram{ram_value}", False)]

    data = getDevicesDataForPage(category, sort_by, how_many_item_on_page, page, brand_filter, ram_filter)
    
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
    if category != "NOT": context |= {"category":category}
    if sort_by != "NOT": context |= {"sort_by":sort_by}
    
    return render(request, "devices.html", context)

def GETtoURL(getDict):
    url = "?"
    for key in getDict:
        url += f"{key}={getDict[key]}&"
    return url[:-1]


def one_device(request, id):
    device = get_object_or_404(Devices, pk=id)
    user_dislikes_device = False
    user_likes_device = False
    like_count = Like.objects.filter(devices_id=device, like=True).count()
    dislike_count = Like.objects.filter(devices_id=device, dislike=True).count()
    if request.user.is_authenticated:
        user_likes_device = Like.objects.filter(user_id=request.user, devices_id=device, like=True).exists()
        user_dislikes_device = Like.objects.filter(user_id=request.user, devices_id=device, dislike=True).exists()
    context = {
        "device" : getDeviceData(id),
        "specification" : getSpecificationData(id),
        "OS_ALL" : getOSAll(id), 
        'user_dislikes_device': user_dislikes_device,
        'user_likes_device': user_likes_device,
        'like_count': like_count,
        'dislike_count': dislike_count,
    }
    return render(request, "device.html", context)
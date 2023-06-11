from django.shortcuts import render
from ..services.os import *
import datetime

def os(request):

    sort_by = request.GET.get('sort_by')
    os_info = getOS_Info(sort_by)
    context = {
        "now" : datetime.datetime.now(),
        "os_info":os_info

    }
    return render(request, "os.html", context)
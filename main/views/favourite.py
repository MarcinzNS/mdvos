from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

from main.models.models import Followed_devices

@ login_required
def favourite_add(request,id):
    fav = Followed_devices.objects.filter(devices_id = id, user_id = request.user.id).exists()
    if fav:
        Followed_devices.objects.filter(devices_id = id, user_id = request.user.id).delete()
    else:
        f = Followed_devices(devices_id_id = id,user_id = request.user)
        f.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def favourites_list(request):
    new = Followed_devices.objects.filter(user_id = request.user)
    return render(request,'favourites.html',{'new':new})
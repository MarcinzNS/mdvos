from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from main.models.models import Devices, Like
from ..services.devices import *


@login_required
def add_like(request, device_id):
    user=request.user
    ADD_Like(user,device_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def add_dislike(request, device_id):
    user=request.user
    ADD_Dislike(user,device_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_like(request, device_id):
    user=request.user
    Remove_Like(user,device_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_dislike(request, device_id):
    user=request.user
    Remove_Dislike(user,device_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
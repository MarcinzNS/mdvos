from django.shortcuts import redirect, render
from main.models import models
from django.http import HttpResponseRedirect
from main.forms import AddDeviceSpecsForm, AddDeviceForm, ChangeDevicePhotoForm
from django.contrib import messages
from django.urls import reverse
from main.services import admin

def remove_device(request, device_id):
    
    if not request.user.is_staff:
        return redirect('error404')
    
    try:
        admin.remove_device(device_id)
        messages.success(request, 'Pomyślnie usunięto produkt')

    except:
        messages.warning(request, 'Nie udało się usunąć produktu')

    return redirect('devices')


def edit_device_info(request, device_id):
    if not request.user.is_staff:
        return redirect('error404')
    
    device = admin.get_device(device_id)
    if not device:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    if request.method == 'POST':

        main_form = AddDeviceForm(request.POST, instance=device)
        specs_form = AddDeviceSpecsForm(request.POST)

        if main_form.is_valid() and main_form.has_changed():
            main_form.save()
        else:
            messages.warning(request, main_form.errors)

        if specs_form.is_valid() and specs_form.has_changed():
            admin.edit_device_specs(specs_form.cleaned_data, device_id)
        else:
            messages.warning(request, specs_form.errors)
    

    context = {'main_form': main_form, 'specs_form': specs_form}
    return HttpResponseRedirect(request.META['HTTP_REFERER'],)


def edit_device_photo(request, device_id):
    if not request.user.is_staff:
        return redirect('error404')

    device = admin.get_device(device_id)
    if not device:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST':
        image_form = ChangeDevicePhotoForm(request.POST, request.FILES, instance=device)

        if image_form.is_valid() and image_form.has_changed():
            image_form.save()
        else:
            messages.warning(request, image_form.errors['image'])
            
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



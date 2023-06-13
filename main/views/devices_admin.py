from django.shortcuts import redirect, render
from main.models import models
from django.http import HttpResponseRedirect
from main.forms import AddDeviceSpecsForm, AddDeviceForm, ChangeDevicePhotoForm
from django.contrib import messages
from django.urls import reverse

def remove_device(request, device_id):
    
    if not request.user.is_staff:
        return redirect('devices')
    
    try:
        device = models.Devices.objects.get(id_device=device_id)
        device.accepted = False
        device.save()
        messages.success(request, 'Pomyślnie usunięto produkt')

    except:
        messages.warning(request, 'Nie udało się usunąć produktu')

    return redirect('devices')


def edit_device_info(request, device_id):
    if not request.user.is_staff:
        return redirect('devices')
    
    device = models.Devices.objects.get(id_device=device_id)
    if not device:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    if request.method == 'POST':

        main_form = AddDeviceForm(request.POST, instance=device)
        specs_form = AddDeviceSpecsForm(request.POST)

        if main_form.is_valid() and main_form.has_changed():
            main_form.save()
        else:
            messages.warning(request, main_form.errors['brand'])

        if specs_form.is_valid() and specs_form.has_changed():
            edit_device_specs(specs_form.cleaned_data, device_id)
        else:
            messages.warning(request, specs_form['model'])
    

    context = {'main_form': main_form, 'specs_form': specs_form}
    return HttpResponseRedirect(request.META['HTTP_REFERER'],)


def edit_device_photo(request, device_id):
    if not request.user.is_staff:
        return redirect('devices')

    device = models.Devices.objects.get(id_device=device_id)
    if not device:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if request.method == 'POST':
        image_form = ChangeDevicePhotoForm(request.POST, request.FILES, instance=device)

        if image_form.is_valid() and image_form.has_changed():
            image_form.save()
        else:
            messages.warning(request, image_form.errors['image'])
            
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def edit_device_specs(specs_data, device_id):
    cpu = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='CPU'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    cpu.value = specs_data['cpu']
    cpu.save()

    ram = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='RAM'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    ram.value = specs_data['ram']
    ram.save()

    screen_size = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='SIZE'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    screen_size.value = specs_data['screen_size']
    screen_size.save()

    battery = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='BATTERY'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    battery.value = specs_data['battery']
    battery.save()

    disk = models.Specification.objects.get(
        spec_type_id=models.Specification_type.objects.get(name='DISC'),
        devices_id=models.Devices.objects.get(id_device=device_id),
    )
    disk.value = specs_data['disk_size']
    disk.save()
from django.shortcuts import render, redirect
from ..forms import AddDeviceForm, AddDeviceSpecsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..services.devices import add_specs_to_device


@login_required(login_url='login')
def add_device(request):
    if request.method == "POST":
        main_form = AddDeviceForm(request.POST, request.FILES)
        specs_form = AddDeviceSpecsForm(request.POST)
        
        if not (main_form.is_valid() and specs_form.is_valid()):
            return render(request, 'add_device.html', {'main_form':main_form, 'specs_form': specs_form})
        
        device = main_form.save()
        add_specs_to_device(specs_form.cleaned_data, device.id_device)

        messages.success(request, "Złożono propozycję dodania urządzenia.")
        return render(request, 'add_device.html', {'main_form': main_form, 'specs_form': specs_form})

            
    main_form = AddDeviceForm()
    specs_form = AddDeviceSpecsForm()
    return render(request, "add_device.html", {'main_form': main_form, 'specs_form': specs_form})

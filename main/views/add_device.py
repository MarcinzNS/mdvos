from django.shortcuts import render, redirect
from ..forms import AddDeviceForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def add_device(request):
    if request.method == "POST":
        form = AddDeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Złożono propozycję dodania urządzenia.")
            return render(request, 'add_device.html', {'form': form})
        
        else:
            return render(request, 'add_device.html', {'form':form})

    form = AddDeviceForm()
    return render(request, "add_device.html", {'form': form})
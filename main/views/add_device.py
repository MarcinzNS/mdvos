from django.shortcuts import render, redirect
from ..forms import AddDeviceForm

def add_device(request):
    if request.method == "POST":
        form = AddDeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = AddDeviceForm()
    return render(request, "add_device.html", {'form': form})
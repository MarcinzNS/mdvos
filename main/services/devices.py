from ..models.models import Devices, Specification
from django.db.models import Q

def getDevicesDataForPage(category, how_many, which_page, brand_filter, ram_filter):
    start = (which_page-1)*how_many
    if category == "NOT":
        devices = list(Devices.objects.values())[start:start+how_many]
    else:
        devices = list(Devices.objects.filter(device_type=category).values())[start:start+how_many]
    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))

    result = []
    for device in devices:
        device_specifications = [spec for spec in specifications if spec['devices_id'] == device['id_device']]
        device_data = {
            'device': 
                device,
            'specifications': 
                {spec['spec_type_id__name']: spec['value'] for spec in device_specifications}
        }
        if len(brand_filter) + len(ram_filter) > 0:
            if device_data['specifications']["RAM"] in ram_filter or device['name'] in brand_filter:
                result.append(device_data)
        else:
            result.append(device_data)

    return {"data": result, "how_many_results": len(devices)}

def getDeviceData(id):
    return Devices.objects.all().filter(id_device=id).values()[0]

def getSpecificationData(id):
    return  Specification.objects.all().filter(devices_id=id).values()[0]

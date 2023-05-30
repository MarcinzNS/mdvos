from ..models.models import Devices, Specification
from django.db.models import Q

def getDevicesDataForPage(category: str, sort_by: str, how_many: int, which_page: int, brand_filter: list, ram_filter: list) -> dict:
    start = (which_page-1)*how_many

    devices = Devices.objects.filter(accepted=True)
    if category != "NOT":
        devices = devices.filter(device_type=category)
    if sort_by != "NOT":
        devices = devices.order_by(sort_by)
    devices = devices.values()[start:start+how_many]

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
            if device_data['specifications']["RAM"] in ram_filter or device['brand'] in brand_filter:
                result.append(device_data)
        else:
            result.append(device_data)

    return {"data": result, "how_many_results": len(result)}

def getDeviceData(id: int) -> dict:
    return Devices.objects.all().filter(id_device=id).values()[0]

def getSpecificationData(id: int) -> dict:
    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))
    device_specifications = {spec['spec_type_id__name']: spec['value'] for spec in specifications if spec['devices_id'] == id}
    return device_specifications

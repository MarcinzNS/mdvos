from ..models.models import Devices, OS, OS_devices, OS_version
from django.db.models import Q

def getOSAll(id: int) -> dict:
    os_all = list(OS_version.objects.filter()
        .values('os_version_id', 'version', 'date_start', 'date_end', 'os_id')
    )
    
    os_all_name = list(OS.objects.values('id_os', 'name'))
    os_data = {}
    
    for os_info in os_all:
        os_id = os_info['os_id']
        os_data[os_info['os_version_id']] = {
            'version': os_info['version'],
            'date_start': os_info['date_start'],
            'date_end': os_info['date_end'],
            'name': next((os_name['name'] for os_name in os_all_name if os_name['id_os'] == os_id), None)
        }

    return os_data





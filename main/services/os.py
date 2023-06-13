from ..models.models import Devices, OS, OS_devices, OS_version
from datetime import datetime
from django.db.models import Q
import json
from django.db.models import Count

def getOSAll(id: int) -> dict:
    os_devices = list(OS_devices.objects.filter(devices_id=id).values_list('os_id__os_version_id', "devices_id"))

    os_all = []
    for os_device in os_devices:
        os_version_id = os_device[0]
        os_versions = list(
            OS_version.objects.filter(os_version_id=os_version_id)
            .values('os_version_id', 'version', 'date_start', 'date_end', 'os_id')
        )
        os_all.extend(os_versions)

    os_all_name = list(OS.objects.values('id_os', 'name'))
    os_data = {}

    for os_info in os_all:
        date_end = os_info['date_end']
        if date_end is None:
            date_end = "Ciągle wspierany"
        os_id = os_info['os_id']
        os_data[os_info['os_version_id']] = {
            'version': os_info['version'],
            'date_start': os_info['date_start'],
            'date_end': date_end,
            'name': next((os_name['name'] for os_name in os_all_name if os_name['id_os'] == os_id), None)
        }

    return os_data

def getOSChart(id: int) -> dict:
    os_devices = list(OS_devices.objects.filter(devices_id=id).values_list('os_id__os_version_id', "devices_id"))

    os_all = []
    for os_device in os_devices:
        os_version_id = os_device[0]
        os_versions = list(
            OS_version.objects.filter(os_version_id=os_version_id)
            .values('os_version_id', 'version', 'date_start', 'date_end', 'os_id')
        )
        os_all.extend(os_versions)

    os_all_name = list(OS.objects.values('id_os', 'name'))
    os_data = {}

    for os_info in os_all:
        os_id = os_info['os_id']
        os_data[os_info['os_version_id']] = {
            
            "start": os_info['date_start'].year if os_info['date_start'] else None,
            "start_m":os_info['date_start'].month if os_info['date_start'] else None,
            "koniec": os_info['date_end'].year if os_info['date_end'] else None,
            "koniec_m":os_info['date_end'].month if os_info['date_end'] else None,
        }

    os_chart_json = json.dumps(os_data)
    return os_chart_json


from ..models.models import Devices, OS_devices, OS_version
from datetime import datetime

def getOS_Info(sort_by=None):
    os_data = {}
    os_all = []
    os_all_name = list(OS.objects.values('id_os', 'name'))

    os_versions = list(OS_version.objects.all()
                       .values('os_version_id', 'version', 'date_start', 'date_end', 'description', 'os_id'))
    os_all.extend(os_versions)

    for os_info in os_all:
        os_id = os_info['os_id']
        date_start = os_info['date_start']
        date_end = os_info['date_end']
        if date_start is None:
            date_start = "System nie został wprowadzony"
            date_end = ""
        if (date_end is None) and (date_start is not None):
            date_end = "Ciągle wspierany"

        devices_count = Devices.objects.filter(os_devices__os_id=os_info['os_version_id']).count()

        os_data[os_info['os_version_id']] = {
            'version': os_info['version'],
            'date_start': date_start,
            'date_end': date_end,
            'description': os_info['description'],
            'name': next((os_name['name'] for os_name in os_all_name if os_name['id_os'] == os_id), None),
            'devices_count': devices_count
        }

    if sort_by:
        sorted_os_data = sort_os_data_custom(os_data, sort_by_name=(sort_by == 'name'), sort_by_version=(sort_by == 'version'),
                                             sort_by_popular=(sort_by == 'devices_count'))
    else:
        sorted_os_data = os_data

    return sorted_os_data



def sort_os_data_custom(os_data, sort_by_name=False, sort_by_version=False, sort_by_popular=False):
    if sort_by_name:
        sorted_os_data = sorted(os_data.items(), key=lambda x: x[1]['name'])
    elif sort_by_version:
        sorted_os_data = sorted(os_data.items(), key=lambda x: x[1]['version'])
    elif sort_by_popular:
        sorted_os_data = sorted(os_data.items(), key=lambda x: x[1]['devices_count'], reverse=True)
    else:
        sorted_os_data = os_data.items()

    return dict(sorted_os_data)




from ..models.models import Devices, Specification, Like, Followed_devices, Specification_type, OS_devices
from django.db.models import Q
from main.models.models import Comment
from django.shortcuts import get_object_or_404

def getDevicesDataForPage(category: str, sort_by: str, how_many: int, which_page: int, brand_filter: list, ram_filter: list, search_filter: str) -> dict:
    start = (which_page-1)*how_many

    devices = Devices.objects.filter(accepted=True)
    if category != "NOT":
        devices = devices.filter(device_type=category)
    if sort_by != "NOT":
        devices = devices.order_by(sort_by)
    devices = devices.values()

    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))


    result = []
    for device in devices:
        name_matches = False
        if search_filter == '':
            name_matches = True
        else:
            try:
                device_name = device["brand"] + device["model"]
                device_name = device_name.replace(" ", "").lower()
                if search_filter in device_name:
                    name_matches = True
            except:
                pass
                
        device_specifications = [spec for spec in specifications if spec['devices_id'] == device['id_device']]
        device_data = {
            'device': 
                device,
            'specifications': 
                {spec['spec_type_id__name']: spec['value'] for spec in device_specifications}
        }
        if len(brand_filter) > 0 and len(ram_filter) > 0 and name_matches:
            try:
                if device_data['specifications']["RAM"] in map(str, ram_filter) and device['brand'] in brand_filter:
                    result.append(device_data)
            except:
                pass
        elif len(ram_filter) > 0 and name_matches:
            try:
                if device_data['specifications']["RAM"] in map(str, ram_filter):
                    result.append(device_data)
            except:
                pass
        elif len(brand_filter) > 0 and name_matches:
            try:
                if device['brand'] in brand_filter:
                    result.append(device_data)
            except:
                pass
        elif name_matches: 
            result.append(device_data)

    return {"data": result[start:start+how_many], "how_many_results": len(result)}

def getDevicesFollowed(id:int):
    devices = Devices.objects.filter(accepted=True)
    devices = devices.values()

    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))
    
    follow = list(Followed_devices.objects.filter(user_id=id).values('devices_id'))
    print(follow)
    result = []
    for device in devices:
        device_specifications = [spec for spec in specifications if spec['devices_id'] == device['id_device']]
        device_data = {
            'device': 
                device,
            'specifications': 
                {spec['spec_type_id__name']: spec['value'] for spec in device_specifications}
        }
        if device['id_device'] in map(lambda x: x['devices_id'], follow):
            result.append(device_data)

    return {"data": result}



def getDeviceData(id: int) -> dict:
    return Devices.objects.all().filter(id_device=id).values()[0]

def getSpecificationData(id: int) -> dict:
    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))
    device_specifications = {spec['spec_type_id__name']: spec['value'] for spec in specifications if spec['devices_id'] == id}
    return device_specifications

def getDeviceLike(request,id: int) ->dict:
    devices= get_object_or_404(Devices,pk=id)
    result = []
    user_dislikes_device = False
    user_likes_device = False
    like_count = Like.objects.filter(devices_id=devices, like=True).count()
    dislike_count = Like.objects.filter(devices_id=devices, dislike=True).count()

    if request.user.is_authenticated:
        user_likes_device = Like.objects.filter(user_id=request.user, devices_id=devices, like=True).exists()
        user_dislikes_device = Like.objects.filter(user_id=request.user, devices_id=devices, dislike=True).exists()


    result = {'user_dislikes_device': user_dislikes_device, 'user_likes_device': user_likes_device,
                     'like_count': like_count,'dislike_count': dislike_count}
    return result

def ADD_Like(user,device_id):
    device = get_object_or_404(Devices, pk=device_id)
     # Sprawdź, czy użytkownik ma już niepolubienie dla tego urządzenia
    existing_dislike = Like.objects.filter(user_id=user, devices_id=device, dislike=True).first()
    if existing_dislike:
        existing_dislike.delete()  # Usuń dislike

    like = Like(user_id=user, devices_id=device, like=True, dislike=False)
    like.save()
    return True

def ADD_Dislike(user,device_id):
    device = get_object_or_404(Devices, pk=device_id)

    # Sprawdź, czy użytkownik ma już like dla tego urządzenia
    existing_like = Like.objects.filter(user_id=user, devices_id=device, like=True).first()
    if existing_like:
        existing_like.delete()  # Usuń like

    dislike = Like(user_id=user, devices_id=device, like=False, dislike=True)
    dislike.save()
    return True

def Remove_Like(user,device_id):
    device = get_object_or_404(Devices, pk=device_id)

    like = Like.objects.filter(user_id=user, devices_id=device, like=True).first()
    if like:
        like.delete()
    return True

def Remove_Dislike(user,device_id):
    device = get_object_or_404(Devices, pk=device_id)

    dislike = Like.objects.filter(user_id=user, devices_id=device, dislike=True).first()
    if dislike:
        dislike.delete()
    return True

def ADD_OS(os_version_form):
    os_version = os_version_form.save(commit=False)
    os_version.accepted = False
    os_version.save()
    os_version_form.save_m2m()

    devices = os_version_form.cleaned_data['devices']  # Pobranie zaznaczonych urządzeń
    for device in devices:
        OS_devices.objects.create(os_id=os_version, devices_id=device)
    return True

def getComments(id: int) -> dict:
    comments = Comment.objects.filter(devices_id=id, main_comment_id='0').values()
    return comments

def getCommentUsername(comment_id: int) -> str:
    comment = Comment.objects.filter(id_comment=comment_id).select_related('user_id').first()
    if comment:
        return comment.user_id.username
    return ""

def getUnderComments(comment_id: int):
    under_comments = Comment.objects.filter(main_comment_id=comment_id).select_related('user_id').values('id_comment', 'text', 'user_id__username')
    return list(under_comments)


def getMCData(id: int) -> dict:
    main_comments = Comment.objects.filter(devices_id=id, main_comment_id=0).select_related('user_id')
    main_comments_data = [{'id_comment': comment.id_comment, 'text': comment.text, 'username': comment.user_id.username} for comment in main_comments]
    return main_comments_data

def getCommentsWithUnderComments(id: int) -> dict:


    main_comments_data = getMCData(id)
    comments = getComments(id)
    comments_username=getCommentUsername(id)
    under_comments = []
    comments_dict = {}

    for comment in comments:
        comment_id = comment['id_comment']
        comments_dict[comment_id] = {
            'id_comment': comment_id,
            'text': comment['text'],
            'username': getCommentUsername(comment_id),
            'under_comments': []
        }

    for main_comment in main_comments_data:
        main_comment_id = main_comment['id_comment']
        if main_comment_id in comments_dict:
            comments_dict[main_comment_id]['under_comments'] = getUnderComments(main_comment_id)


    return list(comments_dict.values())


def add_specs_to_device(specs_data, device_id):
    spec_types = {
        'CPU': 'cpu',
        'RAM': 'ram',
        'SIZE': 'screen_size',
        'BATTERY': 'battery',
        'DISC': 'disk_size',
    }

    devices_id=Devices.objects.get(id_device=device_id)

    for spec_type_name, spec_data_key in spec_types.items():
        id_spec_type = Specification_type.objects.get(name=spec_type_name)
        spec = Specification(
            spec_type_id=id_spec_type,
            value=specs_data[spec_data_key],
            devices_id=devices_id
        )
        spec.save()
    
    return True

def initialForAddDeviceForm():
    device = Devices.objects.get(id_device=id)
    return {
        'brand': device.brand,
        'model': device.model,
        'device_type': device.device_type,
        'release_date': device.premier,
    }

def initialForAddDeviceSpecsForm():
    specification_type_names = ["CPU", "RAM", "SIZE", "BATTERY", "DISC"]
    specifications = Specification.objects.filter(
        devices_id=id,
        spec_type_id__in=Specification_type.objects.filter(name__in=specification_type_names)
    )
    specs_dict = {}
    for specification in specifications:
        specs_dict[specification.spec_type_id.name.lower()] = specification
    return specs_dict

def initialForChangeDevicePhotoForm():
    return {'image': Devices.objects.get(id_device=id).image}




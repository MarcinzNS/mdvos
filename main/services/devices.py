from ..models.models import Devices, Specification ,Like
from django.db.models import Q
from main.models.models import Comment

def getDevicesDataForPage(category: str, sort_by: str, how_many: int, which_page: int, brand_filter: list, ram_filter: list) -> dict:
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

    return {"data": result[start:start+how_many], "how_many_results": len(result)}

def getDeviceData(id: int) -> dict:
    return Devices.objects.all().filter(id_device=id).values()[0]

def getSpecificationData(id: int) -> dict:
    specifications = list(Specification.objects.values('spec_type_id__name', 'value', "devices_id"))
    device_specifications = {spec['spec_type_id__name']: spec['value'] for spec in specifications if spec['devices_id'] == id}
    return device_specifications

def getComments(id: int) -> dict:
    comments = Comment.objects.filter(devices_id=id).values()
    return comments

def getMCid(id: int) -> dict:
    main_comment_ids = Comment.objects.filter(devices_id=id).values('main_comment_id')
    return main_comment_ids


    comments = Comment.objects.filter(devices_id=id).select_related('user_id')
    result = [{'id_comment': comment.id_comment, 'text': comment.text, 'username': comment.user_id.username} for comment in comments]
    return result

#def getUnderComments(id: int) -> dict:
    under_comments = Comment.objects.filter(main_comment_id=id).values()
    return under_comments

def getCommentsUsername(id: int) -> dict:
    comments = Comment.objects.filter(devices_id=id).select_related('user_id')
    result = []
    for comment in comments:
        result.append({
            'id_comment': comment.id_comment,
            'text': comment.text,
            'username': comment.user_id.username if comment.user_id else None
        })
    return result
    comments = Comment.objects.filter(devices_id=id).select_related('user_id')
    result = [{'id_comment': comment.id_comment, 'text': comment.text, 'username': comment.user_id.username} for comment in comments]
    return result

#def getCommentsWithUnderComments(id: int) -> dict:
    comments = getComments(id)
    main_comment_ids = getMCid(id)
    under_comments = getUnderComments(id)
    comments_dict = {}

    for comment in comments:
        comment_id = comment['id_comment']
        comments_dict[comment_id] = {
            'comment': comment,
            'under_comments': []
        }

    for under_comment in under_comments:
        main_comment_id = under_comment['main_comment_id']
        if main_comment_id in comments_dict:
            comments_dict[main_comment_id]['under_comments'].append(under_comment)

    comments_with_under_comments = []
    for comment_id in main_comment_ids:
        comment_id = comment_id['main_comment_id']
        if comment_id in comments_dict:
            comments_with_under_comments.append(comments_dict[comment_id])

    return comments_with_under_comments

    comments = getComments(id)
    main_comment_ids = getMCid(id)
    under_comments = getUnderComments(id)
    comments_dict = {}

    for comment in comments:
        comment_id = comment['id_comment']
        comments_dict[comment_id] = {
            'comment': comment,
            'under_comments': []
        }

    for under_comment in under_comments:
        main_comment_id = under_comment['main_comment_id']
        if main_comment_id in comments_dict:
            comments_dict[main_comment_id]['under_comments'].append(under_comment)

    return comments_dict

    comments = getComments(id)
    under_comments = getUnderComments(id)
    comments_dict = {}
    
    for comment in comments:
        comment_id = comment['id_comment']
        comments_dict[comment_id] = {
            'id_comment': comment_id,
            'text': comment['text'],
            'username': comment['username'],
            'under_comments': []
        }
    
    for under_comment in under_comments:
        main_comment_id = under_comment['main_comment_id']
        comments_dict[main_comment_id]['under_comments'].append(under_comment)
    
    return list(comments_dict.values())

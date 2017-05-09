from django.contrib import auth as django_auth
import base64
from django.http import JsonResponse
from login.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from login.views_if_security import user_sign

def user_auth(request):
    get_http_auth = request.META.get('HTTP_AUTHORIZATION',b'')
    auth = get_http_auth.split()
    try:
        auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')
    except IndexError:
        return 'null'
    username,password = auth_parts[0],auth_parts[2]
    user = django_auth.authenticate(username=username,password=password)
    if user is not None:
        django_auth.logout(request,user)
        return 'success'
    else:
        return 'fail'

def get_event_list(request):
    auth_result = user_auth(request)
    if auth_result == "null":
        return JsonResponse({'status':10011,'message':'user auth null'})
    if auth_result == "fail":
        return JsonResponse({'status':10012,'message':'user auth fail'})
    eid = request.GET.get('eid','')
    name = request.GET.get('name','')
    if eid == '' and name == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status': 200, 'message': 'success', 'data': event})
    if name != '':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

def add_event(request):
    sign_result = user_auth(request)
    if sign_result == 'error':
        return JsonResponse({'status':10011,'message':'request error'})
    elif sign_result == 'sign null':
        return JsonResponse({'status':10012,'message':'user sign null'})
    elif sign_result == 'timeout':
        return JsonResponse({'status':10013,'message':'user sign timeout'})
    elif sign_result == 'sign fail':
        return  JsonResponse({'status':10014,'message':'user sign error'})
    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')
    limit = request.GET.get('limit', '')
    status = request.GET.get('status', '')
    address = request.GET.get('address', '')
    start_time = request.GET.get('start_time', '')
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address,
                             status=int(status), start_time=start_time)
    except ValidationError:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})
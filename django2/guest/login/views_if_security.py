import time,hashlib
def user_sign(request):
    if request.method == "POST":
        client_time = request.POST.get('time','')
        client_sign = request.POST.get('sign','')
    else:
        return 'error'
    if client_time == '' or client_sign == '':
        return 'sign null'
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return 'timeout'
    md5 = hashlib.md5()
    sign_str = client_time + '&Guest-Bugmaster'
    sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()
    if server_sign != client_sign:
        return 'sign fail'
    else:
        return 'sign success'

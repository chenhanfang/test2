from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from login.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):###登录首页
    return render(request,'login/index.html')

def login_action(request):####登录操作
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        # if username == 'admin' and password == 'admin':
            # return HttpResponse('login success!')####之间显示文字信息
            respone = HttpResponseRedirect('/login/event_manage/')####跳转到event_manage
            # respone.set_cookie('user',username,3600)####添加cookie
            request.session['user'] = username####将session信息记录到浏览器
            return respone
            # return HttpResponseRedirect('/login/event_manage/')
        else:
            return render(request,'login/index.html',{'error':'username or password error!'})

@login_required####
# def event_manage(request):
#     # username = request.COOKIES.get('user','')####读取cookie
#     username = request.session.get('user','')###读取浏览器的session
#     return render(request,'login/event_manage.html',{'user':username})
#     # return render(request,'login/event_manage.html')

@login_required###只有登录后才能访问的装饰器，搞不懂为啥不行,使用认证登录auth.authrnicate又可以了
def event_manage(request):####发布会展示
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'login/event_manage.html',{'user':username,'events':event_list})

@login_required
def search_name(request):###发布会搜索
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,'login/event_manage.html',{'user':username,'events':event_list})

@login_required
def guest_manage(request):###嘉宾展示
    guest_list = Guest.objects.all()
    username =request.session.get('user','')
    paginator = Paginator(guest_list,5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,'login/guest_manage.html',{'user':username,'guests':contacts})

@login_required
def search_guests(request):###嘉宾搜索
    username = request.session.get('user','')
    search_name = request.GET.get('realname','')
    guest_list = Guest.objects.filter(realname__contains=search_name)
    return render(request,'login/guest_manage.html',{'user':username,'guests':guest_list})

@login_required
def sign_index(request,eid):####签到页
    event = get_object_or_404 (Event, id=eid)
    return render(request,'login/sign_index.html',{'event':event})

@login_required
def sign_index_action(request,eid):####签到动作
    event = get_object_or_404(Event,id=eid)
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'login/sign_index.html',{'event':event,'hint':'phone error.'})
    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request,'login/sign_index.html',{'event':event,'hint':'event id or phone error！'})
    result1 = Guest.objects.get(phone=phone, event_id=eid)
    if result1.sign:
        return render(request,'login/sign_index.html',{'event':event,'hint':'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone,event_id=eid,).update(sign='1')
        return render(request,'login/sign_index.html',{'event':event,'hint':'sign in success!',
                                                       'guest':result1})


@login_required
def logout(request):####退出登录
    auth.logout(request)
    # response = HttpResponseRedirect('/login/index/')
    # return response
    return render(request,'login/index.html')
# Create your views here.
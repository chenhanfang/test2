from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models
def index(request):
    # return HttpResponse('Hello , world')
    # article = models.Article.objects.get(pk=1)####获取索引为1的数据
    # articles = models.Article.objects.all()####获取所有列表数据

    return render(request,'login/index.html')

# def login_action(request):
# @login_required####登录装饰器，只要登录之后才能看到
def event_manage(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin':
            # return HttpResponse('login success!')
            # return HttpResponseRedirect('/event_manage/')
            return  render(request,'login/event_manage.html')
            # response = render(request,'login/event_manage.html')
            # response.set_cookie('user', username, 3600)####添加浏览器cookie
            # response.session['user'] = username####将session信息记录到浏览器
            # username = request.COOKIES.get('user','')###读取cookie
            # username = request.session.get('user','')####读取session
            # return render(request,'login/event_manage.html',{ 'user': username })
        else:
            return render(request,'login/index.html',{'error':'username or password error!'})

# def event_manage(request):#####从login_action跳转过了不行不知道为啥
#     return render(request,'login/event_manage.html')
# Create your views here.

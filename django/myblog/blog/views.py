from django.shortcuts import render###渲染
from django.http import HttpResponse
from . import models

def index(request):
    # return HttpResponse('Hello , world')
    # article = models.Article.objects.get(pk=1)####获取索引为1的数据
    articles = models.Article.objects.all()####获取所有列表数据

    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):###展示文章
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/editpage.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/editpage.html',{'article':article})

def edit_action(request):
    title =request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        return render(request,'blog/index.html',{'articles':articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})
# Create your views here.

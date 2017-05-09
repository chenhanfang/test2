from django.conf.urls import url,include
from django.contrib import admin
from . import views as bv

urlpatterns = [
    url(r'^index/$',bv.index),
    url(r'^admin',admin.site.urls),
    url(r'^article/(?P<article_id>[0-9]+)$',bv.article_page,name='article_page'),#####匹配文章索引
    # url(r'^edit/$',bv.editpage,name='edit_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',bv.edit_page,name='edit_page'),
    url(r'^edit/action$',bv.edit_action,name='edit_action'),

]
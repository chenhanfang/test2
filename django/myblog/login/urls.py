from django.conf.urls import url,include
from django.contrib import admin
from . import views as bv

urlpatterns = [
    url(r'^index/$',bv.index),
    # url(r'^login_action/$',bv.login_action),
    url(r'^event_manage/$',bv.event_manage),


]
from django.conf.urls import url,include
from . import views
from . import views_if
from . import views_if_sec

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^$',views.index),
    url(r'^accounts/login/$',views.index),
    url(r'^login_action/$',views.login_action),
    url(r'^event_manage/$',views.event_manage),
    url(r'^search_name/$',views.search_name),
    url(r'^search_guests/$',views.search_guests),
    url(r'^guest_manage/$',views.guest_manage),
    url(r'^sign_index/(?P<eid>[0-9]+)/$',views.sign_index),
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$',views.sign_index_action),
    url(r'^logout/$',views.logout),
    #login system interface:
    url(r'^add_event/',views_if.add_event,name='add_event'),
    url(r'^add_guest/',views_if.add_guest,name='add_guest'),
    url(r'^get_event_list/',views_if.get_event_list,name='get_event_list'),
    url(r'^search_guest/',views_if.search_guest,name='search_guest'),
    url(r'^user_sign/',views_if.user_sign,name='user_sign'),
    url(r'sec_get_event_list',views_if_sec.get_event_list,name='sec_get_event_list'),
    url(r'sec_add_event/',views_if_sec.add_event,name='sec_add_event')
]
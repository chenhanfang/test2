from django.contrib import admin
from login.models import Event,Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name']###搜索栏
    list_filter = ['status'] ###过滤器
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone']
    list_filter = ['sign']

admin.site.register(Event,EventAdmin)####在admin中展示Event,Guest的数据
admin.site.register(Guest,GuestAdmin)


# Register your models here.

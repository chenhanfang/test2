from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):#####配置类
    list_display = ('title','content','pub_time')######显示更多内容
    list_filter = ('pub_time', )######时间过滤器

admin.site.register(Article,ArticleAdmin)####引入数据库




# Register your models here.

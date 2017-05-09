from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now = True)####自动的,null=True在具体内容中展示，进行修改时间，
######修改的时候需要python manage.py makemigrations     和python manage.py migrate
    def __str__(self):####显示标题，python2中是_unicode__
        return self.title






# Create your models here.

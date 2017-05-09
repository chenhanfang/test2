from django.test import TestCase
from login.models import Event
from django.contrib.auth.models import User
# class IndexPageTest(TestCase):
#     def test_index_page_render_index_template(self):
#         response = self.client.get('/login/index/')
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'login/index.html')

class EventManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','123@163.com','admin123456')
        Event.objects.create(name='xiaomi6',limit=2000,address='beijing',
                             status=1,start_time='2017-5-1 10:00:00')
        self.login_user = {'username':'admin','password':'admin123456'}

    def test_event_manage_success(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/event_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'xiaomi6',response.content)
        self.assertIn(b'beijing',response.content)

    def test_event_manage_search_success(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/search_name/',{'name':'xiaomi6'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'xiaomi6',response.content)
        self.assertIn(b'beijing',response.content)


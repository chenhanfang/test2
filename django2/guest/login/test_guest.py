from login.models import Guest,Event
from django.test import TestCase
from django.contrib.auth.models import User

class GuestTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','123@163.com','admin123456')
        Event.objects.create(id=1,name='xiaomi6',limit=2000,address='beijing',
                             status=1,start_time='2017-5-1 10:00:00')
        Guest.objects.create(id=18,realname='hen',event_id=1,phone='18329176957',
                             email='123@163.com',sign=1)
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_guest_manage_success(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/guest_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'hen',response.content)
        self.assertIn(b'18329176957',response.content)
    def test_guest_search_success(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/search_guests/',{'realname':'hen'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'chen',response.content)
        self.assertIn(b'18329176957',response.content)

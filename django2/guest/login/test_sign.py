from django.test import TestCase
from login.models import Event,Guest
from django.contrib.auth.models import User

class SignTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','123@163.com','admin123456')
        Event.objects.create(name='xiaomi5',id=1,limit=2000,address='beijing',
                             status=1,start_time='2017-5-1 10:00:00')
        Event.objects.create(name='meizu7',id=2,limit=3000,address='shanghai',
                             status=1,start_time='2017-5-3 14:00:00')
        Guest.objects.create(realname='chen',event_id=1,phone='18329176957',
                             email='123@163.com',sign=1)
        Guest.objects.create(realname='li',event_id=2,phone='17391825397',
                             email='124@163.com',sign=0)
        self.login_user={'username':'admin','password':'admin123456'}

    def test_sign_index_phone_null(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/sign_index_action/1/',{'phone':''})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'phone error',response.content)

    def test_sign_index_phone_id_error(self):####老是报错，有问题
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/sign_index_action/1/',{'phone':'17391825'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'event id or phone error!',response.content)

    def test_sign_index_has(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/sign_index_action/1/',{'phone':'18329176957'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'user has sign in.',response.content)

    def test_sign_index_success(self):
        response = self.client.post('/login/login_action/',data=self.login_user)
        response = self.client.post('/login/sign_index_action/2/',{'phone':'17391825397'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'sign in success!',response.content)
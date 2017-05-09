#_*_ coding:utf-8 _*_
from django.test import TestCase
from login.models import Event,Guest
from django.contrib.auth.models import User

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1,name='apple plus7 event',
                             status=True,limit=2400,address='beijin',start_time='2017-08-31 10:00:00')
        Guest.objects.create(id=1,realname='chen',event_id=1,
                             phone='18329176957',email='123@163.com',sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='apple plus7 event')
        self.assertEqual(result.limit,3000)
        self.assertTrue(result.status)

    def test_guest_model(self):
        result = Guest.objects.get(realname='chen')
        self.assertEqual(result.phone,'18329176957')
        self.assertFalse(result.sign)

class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','123@163.com','admin123456')

    def test_add_admin(self):
        user = User.objects.get(username='admin')
        self.assertEqual(user.username,'admin')
        self.assertEqual(user.email,'123@163.com')

    def test_login_action_username_password_null(self):
        test_data = {'username':'','password':''}
        response = self.client.post('/login/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error!',response.content)

    def test_login_action_username_password_error(self):
        test_data = {'username':'han','password':'admin123456'}
        response = self.client.post('/login/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error!',response.content)

    def test_login_action_success(self):
        test_data = {'username':'han','password':'chz970916'}
        response = self.client.post('/login/login_action',data=test_data)
        self.assertEqual(response.status_code,302)####在网页上打开的状态码是302，但是python manage.py test运行的是301


# Create your tests here.

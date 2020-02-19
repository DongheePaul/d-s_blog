from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class LoginAndLogout(TestCase):
    def setUp(self):
        self.client = Client()
        u = User.objects.create_user('test_user', 'password1')
        u.save()

    def test_login_post(self):
        response = self.client.post("/accounts/login/", {"username": "test_user" ,"password": "password1", "next": "/"}, follow=True)
        self.assertEqual(response.status_code, 200) 



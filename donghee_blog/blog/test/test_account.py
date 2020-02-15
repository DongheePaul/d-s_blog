from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class AccountTest(TestCase):
  # 로그인 테스트s./man
  def test_login(self):
    client = Client()
    user = User.objects.create_user(username='donghee',password='1234')
    response = client.post('/login',{'username':'donghee', 'password':'1234'})
    self.assertEqual(response.status_code, 200) 
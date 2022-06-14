from urllib import response
from django.test import TestCase
from django.urls import reverse, resolve
from ShiftManagementApp.views import home
from ShiftManagementApp.models import User,UserManager

class LoginpageTest(TestCase):
    def test_get_status_code_index(self):
        """ログインページにアクセスしたときのステータスコードが200であることを確認"""
        response = self.client.get(reverse('ShiftManagementApp:Login'))
        self.assertEqual(response.status_code,200)

class Calendartest(TestCase):
    def setUp(self):
        """テストログイン用ユーザを作成してログイン維持する"""
        shop_id = 0
        username = 'testuser'
        default_position = True
        email = 'test@mail.com'
        password = 'testpassword'
        is_edit_mode = True

        self.user = User.objects.create_user(
            username,
            email,
            password,
            shop_id=shop_id,
            default_position=default_position,
            is_edit_mode=is_edit_mode
            )

        result_login = self.client.login(email=email,password=password)
        print(f"result_login:{result_login}")

    def test_indexpage_access(self):
        """homeページの表示したときのレスポンスコードが200かどうか確認"""
        response = self.client.get(reverse('ShiftManagementApp:index'))
        self.assertEqual(response.status_code,200)
    
    def test_post_calendar(self):
        pass

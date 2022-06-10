from django.test import TestCase
from django.urls import reverse, resolve
from ShiftManagementApp.views import home

class Indextest(TestCase):
    def test_get_status_code_index(self):
        """ログインページにアクセスしたときのステータスコードが200であることを確認"""
        response = self.client.get(reverse('ShiftManagementApp:Login'))
        self.assertEqual(response.status_code,200)
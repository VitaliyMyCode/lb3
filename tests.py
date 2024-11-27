
from django.test import TestCase

class SimpleTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Ожидает успешный ответ
        self.assertContains(response, "Home Page")  # Проверяет содержимое ответа
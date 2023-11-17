from server import app
from tinydb import TinyDB

import unittest


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.test_db = TinyDB('test_database.json')

    def tearDown(self):
        self.test_db.drop_table('test_database.json')
        self.test_db.close()

    def test_first_sample(self):
        tester = app.test_client(self)
        # в url запросе знак '+' замен '%2B' так как возникала ошибка передачи в строке спец символа
        response = tester.post(
            "/get_form?user_email=2819815@mail.ru&user_phone=%2B7495734-92-00&user_order_date=17.03.1988&user_text=Мне кококолу без льда.&same_data=это просто лишний текст")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 'my_form')

    def test_second_sample(self):
        tester = app.test_client(self)
        # в этом примере сделана ошибка в номере телефона для вывода другой формы
        response = tester.post(
            '/get_form?user_email=2819815@mail.ru&user_phone=+7-123-456&user_order_date=17.03.1988&user_text=Мне кококолу без льда.&same_data=это просто лишний текст')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 'order_form')

    def test_third_sample(self):
        tester = app.test_client(self)
        # в этом примере возвращаем обработанные пользовательские данные
        response = tester.post('/get_form?user_text=это просто лишний текст')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [['user_text', 'text']])


if __name__ == '__main__':
    unittest.main()

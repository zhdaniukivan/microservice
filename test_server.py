from server import app

import unittest



class BasicTestCase(unittest.TestCase):

    def test_first_sample(self):
        tester = app.test_client(self)
        response = tester.post('/get_form?user_email=2819815@mail.ru&user_phone=+7 495 734-92-00&user_order_date=17.03.1999&user_text=Мне кококолу без льда.&same_data=это просто лишний текст')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"form_name":"user_data"}\n')

    def test_second_sample(self):
        tester = app.test_client(self)
        response = tester.post('/get_form?user_email=2819815@mail.ru&'
                               'user_order_date=17.03.1988&user_text=Мне кококолу без льда.&same_data='
                               'это просто лишний текст')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"form_name":"user_data"}\n')


if __name__ == '__main__':
    unittest.main()

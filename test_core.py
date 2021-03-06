# Importamos nosso app
from app import wordfy
from num2words import num2words
# Importamos a biblioteca de testes
import unittest
import random


class TestHomeView(unittest.TestCase):

    def setUp(self):
        app = wordfy.test_client()
        self.response = app.get('/94587')

    # status code 200
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # test numbers
    def test_numbers(self):
        txt = self.response.json['extenso']
        self.assertEqual('noventa e quatro mil e quinhentos e oitenta e sete', txt)

    # test negatives
    def test_negative(self):
        app = wordfy.test_client()
        self.response = app.get('/-12345')
        self.assertEqual('menos doze mil e trezentos e quarenta e cinco', self.response.json['extenso'])

    # test erro
    def test_error(self):
        app = wordfy.test_client()
        self.response = app.get('/1a2b3')
        self.assertEqual(404, self.response.status_code)

    # test aleatorio
    def test_random(self):
        number = random.randint(-99999,99999)
        app = wordfy.test_client()
        self.response = app.get('/'+str(number))
        self.assertEqual(num2words(number, lang='pt_BR').replace(', ',' e '), self.response.json['extenso'])


import unittest
from spi import Spisok
#как запустить тест по коду из другого файла?

class Test_Spisok(unittest.TestCase):
    def test_dell(self):
        sp1 = Spisok()
        self.assertNotEqual(sp1.dell(1), {'name': 'Jon',
    'last_name': 'RT',
    'email': 'gt.ru',
    'number': 768,
    'job': 'actor'}, 'метод не работает')

class Test_adress_book(unittest.TestCase):
    def test_add(self):
        sp1 = Spisok()
        a = {'name': 'Test', 'last_name': 'Test', 'email': 'Test', 'number': 'Test', 'job': 'Test'}
        self.assertEqual(sp1.add(a), {'name': 'Test', 'last_name': 'Test', 'email': 'Test', 'number': 'Test', 'job': 'Test'})


# if __name__ == '__main__':
#     unittest.main()

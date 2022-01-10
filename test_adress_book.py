import unittest
from spi import Spisok
#как запустить тест по коду из другого файла?

class Test_adress_book(unittest.TestCase):
    def test_dell(self):
        sp1 = Spisok()
        self.assertNotEqual(sp1.dell(1), {'name': 'Jon',
    'last_name': 'RT',
    'email': 'gt.ru',
    'number': 768,
    'job': 'actor'}, 'метод не работает')



    # def test_see(self):
    #     n = '3'
    # def add(self):
    #     n = '1'
    #     self.name = 'Test'
    #     self.last_name = 'Test'
    #     self.email = 'Test'
    #     self.number = 'Test'
    #     self.job = 'Test'


# if __name__ == '__main__':
#     unittest.main()

import unittest

#как запустить тест по коду из другого файла?

class Test_adress_book(unittest.TestCase):
    def see(self):
        n = '3'
    def add(self):
        n = '1'
        self.name = 'Test'
        self.last_name = 'Test'
        self.email = 'Test'
        self.number = 'Test'
        self.job = 'Test'


if __name__ == '__main__':
    unittest.main()

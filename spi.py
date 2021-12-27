
a1 = {
    'name': 'Vasy',
    'last_name': 'Poo',
    'email': 'poo.ru',
    'number': 321,
    'job': 'teacher'}
a2 = {
    'name': 'Oly',
    'last_name': 'GR',
    'email': 'gr.ru',
    'number': 345,
    'job': 'teacher'}
a3 = {
    'name': 'Jon',
    'last_name': 'RT',
    'email': 'gt.ru',
    'number': 768,
    'job': 'actor'}
a4 = {
    'name': 'Ivan',
    'last_name': 'ivan',
    'email': 'ivan.ru',
    'number': 876,
    'job': 'singer'}
a5 = {
    'name': 'Mari',
    'last_name': 'Smith',
    'email': 'smith.ru',
    'number': 567,
    'job': 'manager'}


class Spisok:
    sp = [a1, a2, a3]
    def see(self):
        for i in range(len(self.sp)):
            print(self.sp[i].__dict__)
    def dell(self):
        self.see()
        x = int(input('введите номер словаря для удаления '))
        del self.sp[x]
        self.see()
    def add(self, a):
        self.sp.append(a)


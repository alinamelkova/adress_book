# import json
# import requests


from spi import Spisok
from pe import People


while True:
    s = Spisok()
    n = input('1.add, 2.dell, 3. see, 4.очистка файла, 5.редактирование:  ')
    if n == '1':
        a = People()
        r = '; '.join([f'{key.capitalize()}: {value}' for key, value in a.__dict__.items()])
        print(r)
        s.add(a)
        with open('adress_book.txt', 'a') as file:
            file.write(r + '\n')  #
            file.close()

    elif n == '2':
        with open('adress_book.txt', 'r'):
            s.dell()
    elif n == '3':
        # s.see()
        with open('adress_book.txt', 'r') as file:
            print(file.read())
            file.close()
    elif n == "4":
        with open('adress_book.txt', 'w') as file:
            file.close()
    elif n == '5':
        with open('adress_book.txt', 'r') as file:

    else:
      break


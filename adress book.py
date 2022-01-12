from pe import People
from spi import Spisok
from func import *


while True:
    s = Spisok()
    n = input('1.add, 2.dell, 3. see, 4.очистка файла, 5.редактирование:  ')
    if n == '1':
        a = People()
        r = '; '.join([f'{key.capitalize()}: {value}' for key, value in a.__dict__.items()])
        print(r)
        s.add(a)
        awrite(r)
    elif n == '2':
        with open('adress_book.txt', 'r'):
            s.dell()
    elif n == '3':
        read()
    elif n == "4":
        with open('adress_book.txt', 'w') as file:
            file.close()
    elif n == '5':
        file = open('adress_book.txt', 'r')
        spp = [] #создание списка,куда запишется содержимое файла
        translate(file, spp)
        d = input('Введите номер телефона, который хотите отредактировать ')
        print("Было ", next(x for x in spp if x['Number'] == d)) #выводит  с  Number = d
        edil_slovari(spp,d)
        write(spp)
    else:
      break


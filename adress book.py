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
        file = open('adress_book.txt', 'r')
        spp = [] #создание списка,куда запишется содержимое файла
        for line in file:
            b = []
            b = line.rstrip('\n').split(';')
            sl = {} #создание словаря куда записывается содержимое одной строки
            for v in range(len(b)):
                key, value = b[v].split(': ')
                sl[key] = value
            spp.append(sl)
        print(spp)
        d = input('Введите номер телефона, который хотите отредактировать ')
        print(next(x for x in spp if x[' Number'] == d)) #выводит  с  Number = d
        e = next(x for x in spp if x[' Number'] == d)
        # f = {input('Введите ключ и значение, которое хотите отредактировать ')}
        e.update({'Name': 'AAA', ' Last_name': 'AAA'})
        print(e)

        # r = '; '.join([f'{key.capitalize()}: {value}' for key, value in e.__dict__.items()])
        s.add(e) #записывает неизмененное значение
        # print(r)
        # with open('adress_book.txt', 'a') as file:
        #     file.write(r + '\n')  #
        #     file.close()








    else:
      break


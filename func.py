def read():
    with open('adress_book.txt', 'r') as file:
        print(file.read())
        file.close()

def awrite(r): #дозапись данных в файл (добавляется в конец новые данные)
    with open('adress_book.txt', 'a') as file:
        file.write(r + '\n')  #
        file.close()

def translate(file, spp): #перевод содержимого файла в словари по строчно
    for line in file:
        b = []
        stroka = line
        stroka = stroka.replace(" ", "")
        b = stroka.rstrip('\n').split(';')
        sl = {}  # создание словаря куда записывается содержимое одной строки
        for v in range(len(b)):
            key, value = b[v].split(':')
            sl[key] = value
        spp.append(sl)
    print(spp)

def write(spp): #запись данных в файл (все содержимое файла перезаписывается)
    with open('adress_book.txt', 'w') as file:
        for i in spp:
            r = '; '.join([f'{key.capitalize()}: {value}' for key, value in i.items()])
            file.write(r + '\n')
        file.close()

def edil_slovari(spp, d): #редактирует словарь
    for i in spp:  # находит нужный словарь(i) в списке(spp)
        if i['Number'] == d:
            # i.update({input()})
            i.update({'Name': 'w', 'Last_name': 'w'})
            print('Стало ', i)
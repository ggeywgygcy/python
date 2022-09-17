#  Игра "КРЕСТИКИ-НОЛИКИ"

# ппапар
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# hgh
import random
# uju
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ 
# hbhh
def db(h1):
    # эта функция выводит на экран игровое поле
    # клетки корого будут заполнятся

    # "board" - это список в котором хранится 10 строк
    # для прорисовки игрового поля (индекс 0 игнорируется)

    print(h1[7]+'|'+h1[8]+'|' +h1[9])
    print('-+-+-')
    print(h1[4]+'|'+h1[5]+'|' +h1[6])
    print('-+-+-')
    print(h1[1]+'|'+h1[2]+'|' +h1[3])
 
def pl():
    # предложи игрокуввести букву, которую он выбирает
    letter = ''
    while not (letter=='X' or letter=='O'):
        print(''' Выберите Х или О 
        для выбора введите соответственно Х или О
        на англ. раскладке. ''')

        letter = input().upper()

        if letter == 'x':
            return ['X','O']
        else:
            return ['O','X']

def kch():
    # случайным образом выбираем ктот будет ходить первым
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'
    
def goldexpiriensreqiem(per1,p2,p4):
    per1[p4] = p2

def kaknazvat(bd,lt):
    return ((bd[1] == lt and bd[2] == lt and bd[3] == lt) or 
           (bd[4] == lt and bd[5] == lt and bd[6] == lt) or 
           (bd[7] == lt and bd[8] == lt and bd[9] == lt) or
           (bd[7] == lt and bd[4] == lt and bd[1] == lt)or
           (bd[8] == lt and bd[5] == lt and bd[2] == lt)) 
           


    

# tcu
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# FF


per1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
db(per1)
print(kaknazvat(per1,'X'))
per1[9] = 'X'
per1[6] = 'X'
per1[3] = 'X'
db(per1)
print(kaknazvat(per1,'X'))
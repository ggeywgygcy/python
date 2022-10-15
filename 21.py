#  Игра "КРЕСТИКИ-НОЛИКИ"

# ппапар
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# hgh
import random
from this import s

# uju
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ 
# hbh

def intro():
    print('Приветствую тебя! Вы играете в игру "21"')
    print() 
    print('Создатель анонимен')

def voprosPravil():
    while True:
        print('Хотите посмотреть правила пред игрой?');
        otvet = input()
        otvet = otvet.lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'Д') or (otvet == 'l'):
            return True
        elif (otvet == 'ytn') or (otvet == 'нет') or (otvet == 'н'):
            return False
        else:
            print('Программа не поняла ответ!')
            

def kubiki():
    kub = ('''
 _________
|         |
|         |
|         |
|         |
|_________|

 _________
|         |
|         |
|    *    |
|         |
|_________|

 _________
|         |
|         |
|   **    |
|         |
|_________|

 _________
|         |
|   * * * |
|         |
|         |
|_________|

 _________
|         |
|  ****   |
|         |
|         |
|_________|

 _________
|         |
|  *****  |
|         |
|         |
|_________|

 _________
|         |
| ******  |
|         |
|         |
|_________|
    
        ''')

def vivodPoiya(kubiki):










def brosokKubika(kub1,kub2):
    kub1 = random.randint(1,6)
    kub2 = random.randint(1,6)

    if kub1 == kub2:
        same_num = True
    else:
        same_num = False
    return same_num 

def Pravila():
    print('у меня не получается нормально написать правила')

def again():
    while True:
        print('Хотите играть опять?(да или нет)')
        guess = input()
        guess = guess.lower()
        # проверяем ответ на совпадение со следующими фразами
        # "Да","да","д"
        # усли есть совпадение  то переменной присваиваем значение True
        # и прерываем цикл командой return
        if (guess == 'да') or (guess == 'д') or (guess == 'Да'):
            return True
        # проверяем ответ на совпадение со следующими фразами
        # "Нет","нет","н"
        # усли есть совпадение  то переменной присваиваем значение False
        # и прерываем цикл командой return
        elif (guess == 'нет') or (guess == 'Нет') or (guess == 'н'):
            return False
        # если совпадения с первыми двумя случаями нет
        # говорим пользователю, что не поняли его ответа
        else:
            print('Я не понял ответа')
            return guess

# hiuvhuthbhghtiuh
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
# BVBBGBVITBIVBIHTB

otvet = voprosPravil()
if otvet:
    Pravila()





    






























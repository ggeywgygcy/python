#  Игра "КРЕСТИКИ-НОЛИКИ"

# ппапар
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# hgh
import random
from this import s
# uju
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ 
# hbh

def F1():


def F2():
    print('Приветствую тебя! Вы играете в игру "21"')
    print() 
    print('Создатель засекречен')
    print()
    print('Правила:')

def F3(per1,per2):
    kub1 = random.randint(1,2)
    kub2 = random randint(1,2)

    if kub1 == kub2:
        same_num = True
    else:
        same_num = False
    return same_num

def F4(per1,per2):



def again():
    # сщздание бесконечного цикла
    while True:
        # задаём вопрос и получаем ответ
        print('Хотите играть опять?')
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


    






























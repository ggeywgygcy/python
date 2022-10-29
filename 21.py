#  Игра "КРЕСТИКИ-НОЛИКИ"

# ппапар
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# hgh
import random
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
    kub = ['''
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
    
        ''']
    return kub

def vivodPoiya(per1):
    per1 = kubiki()
    return per1


    
def brosok():
    kub1 = random.randint(1,6)
    kub2 = random.randint(1,6)
    zk = []
    zk.append(kub1)
    zk.append(kub2)
    return zk

def Pravila():
    print('''Вы играете против компьтера
    У вас есть кубики. Кидайте их чтобы выиграть.
    Вы должны набрать больше очков чем компьтер.
    Если наберёте очков больше вы выйграли, если меньше то вы проиграли.
    Ничья будет если вы наберёте очки равные очкам компьютера.
    Набрав очки больше числа 21, то вы автоматически проигрываете, а если компьтер набирает 
    количество больше числа 21 то вы выигрываете, а он проигрывает.
    Удачи в игре!
    ''')

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

def displai(gamer,img,k1,k2,summaCh,summaK):
    print(gamer)
    print()
    print(img[k1])
    print(img[k2])
    print('Ваши очки: '+str(summaCh)+ 'У компьтера:' +str(summaK)+'')

# hiuvhuthbhghtiuh
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
# BVBBGBVITBIVBIHTB


otvet = voprosPravil()
if otvet:
    Pravila()

kub = kubiki()
game = True

while game:
    kub1,kub2 = brosok()
    Brosaet = 'Человек'
    summaCh = 0
    summaK = 0
    summa = summaCh + kub1 + kub2

displai(gamer,img,k1,k2,summaCh,summaK)

intro()
 
   







    






























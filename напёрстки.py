# ====================
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ====================
import random  
# ====================
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ 
# ==================================

# =========================
def nastroyki():
    print('ИГРА "напёрстки"')
    print()
    print('Автор: Неизвестен')
    print()
    print('Версия 1.0')
    print()

    print('Введите сколько у игрока денег')
    dengi = input()
    while True:
        if dengi.isdigit():
            dengi = int(dengi)
            break
        else:
            print('Надо вводить только цифры')
            dengi = input()

    print('Введите размер минимальной ставки')
    minStavka = input()
    while True:
        if minStavka.isdigit():
            minStavka = int(minStavka)
            break
        else:
           print('Надо вводить цифры')
           minStavka = input()

    return [dengi,minStavka]

def intro():
    print('''       Вы пришли на рынок.
    
    На рынке вы видите человека сидящего за столом.
    
    Перед ним три напёрстка и маленький шарик.
    
    Заинтересовавшись вы подходите к человеку.
    
    Он предлагает вам испытать свою удачу

    и сыграть с ним на деньги''')

def proverka(dengi,minStavka):
    print('Сделайте вашу ставку')
    stavka = input()
    while True:
        if stavka.isdigit():
            # переводи строку в число
            stavka = int(stavka)
            # проверяем что ставка больше минимальной 
            if stavka > minStavka:
                # проверяем что ставка меньше количества денег у игрока
                if stavka > dengi:
                    print('ставка не может быть больше суммы денег у игрока')
                    stavka = input()
                else:
                    break
            else:
                print('Ставка не может быть меньше минимальной')
                stavka = input()
        else:
            print('Надо вводить только цифры')
            stavka = input()
    return stavka 
def sravnenie(sharik,naperstok):
    if sharik == naperstok:
        naperstok = True   
    else:
        naperstok = False
    return naperstok

def intro2():
    print('''       После того как вы сделали ставку , 
    
    ведущий начинает крутить наперстки по столу, потом он остановился
    
    и предложил выбрать напёрсток в котором по твоему мнению лежит шарик.''')
def vibor():
    print('Выберите напёрсток в котром лежит шарик')
    nap = input()
    while True:
        if nap.isdigit():
           if (nap in '123') and (len(nap)==1):
               nap = int(nap)
               break
           else:
               print('Нужно вводить только цифры от одного до трёх!')
               nap = input()
        else:
            print('Надо вводить только цифры')
            nap = input()
    return nap

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

 # hgekfgfgyiggyggg
 # ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
 # FRGGGGGGYEGYFGYGY

    
many,minBig = nastroyki()
intro()

while True:
    stavkaIgroka = proverka(many,minBig)
    intro2()
    dbz = random.randint(1,3)
    dbS = vibor()
    if sravnenie(dbz,dbS):
        print('Ты выйграл, ураааааааааааааааааа')
        many = many + stavkaIgroka
    else:
        print('Ххахахахахахахахахахахахах, ты проиграл -10000;')
        many = many - stavkaIgroka

    if many > minBig:
        # зададим вопрос хочет ли человек играть ещё
        if again():
            print('Продолжаем играть. В наличии'+str(many))
        else:
            print('Хорошо. Игра закончена. В наличии '+str(many))
            break
    else:
        print('У вас осталось денег меньше мрнимальной ставки.')
        print('В наличии'+str(many)+'. Игра будет завершена')
        break
print(many)
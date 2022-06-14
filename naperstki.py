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
                print('Ставка не может быть больше минимальной')
                stavka = input()
        else:
            print('Надо вводить только цифры')
            stavka = input()
    return stavka 

 # hgekfgfgyiggyggg
 # ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
 # FRGGGGGGYEGYFGYGY

many,minBig = nastroyki()
intro()
stavkaIgroka = proverka(many,minBig)
 
# game holodno goryacho

#ffurefcfe
# РАЗДЕЛ ИМПОРТА НОЛЕЙ
#HGHUTHGU
import random
#hfuiogi5gifgifgiyg5
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# V4EVRYIFIYVE

KOLCHISEL = 3
KOLPOPITOK = 5

def generaciya():
    cifri = list(range(10))
    random.shuffle(cifri)
    sicretCif = ''
    for a in range(KOLCHISEL):
        sicretCif += str(cifri[a])
    return sicretCif

def podskazki(ch_game,ch_secret):
    if ch_game == ch_secret:
        return 'Вы угадали!'

    podskazka = []
    for b in range(len(ch_game)):
        if ch_game[b] == ch_secret[b]:
            podskazka.append('горячо')
        elif ch_game[b] in ch_secret:
            podskazka.append('тепло')
    
    if len(podskazka) == 0:
        return 'холодно'

    podskazka.sort()
    return ' '.join(podskazka)

def proverka_ch(Num):
    if Num == '':
        return False

    if Num not in '0 1 2 3 4 5 6 7 8 9' .split():
        return False

    return True

def again():    
    while True:
        # задаём вопрос и получаем ответ
        print('Хотите играть опять?')
        guess = input()
        # проверяем ответ на совпадение со следующими фразами
        # "Да","да","д"
        # усли есть совпадif i = [2]подсказок...ение print(podskazki('123','321')) то переменной присваиваем значение True
        # и прерываем цикл командой return
        if (guess == 'да') or (guess == 'д') or (guess == 'Да'):
            return True
        # проверяем ответ на совпадение со следующими фразами
        # "Нет","нет","н"if i = [1]
        # усли есть совпадение  то переменной присваиваем значение False
        # и прерываем цикл команeдой return
        elif (guess == 'нет') or (guess == 'Нет') or (guess == 'н'):
            return False
        # если совпадения с первыми двумя случаями нет
        # говорим пользователю, что не поняли его ответа
        else:
            print('Я не понял ответа')

#goerogoutg
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#EHGOUREUHGIG

print('Я загадаю %s-х значное число, которое вы должны отгадать.' %(KOLCHISEL))
print('Я вам дам несколько for i in Num:')
print('Когжа я вам говорю     Это обозначает')
print(' Холодно        Не одна цифра не отгадана')
print(' Тепло         Одна цифра не отгадана, но не отгадана позиция')
print(' Горячо        Ничего не отгадано')

while True:
    secretCif = generaciya()
    
    print('Итак. Я загадал число, у вас есть %s попыток для того что бы отгадать это число' %(KOLPOPITOK)) 

    

    popytka = 1
    while popytka <= KOLPOPITOK:
        chisloIg = ''
        while len(chisloIg) != KOLCHISEL or not proverka_ch(chisloIg):
            print('попытка номер %s:' %(popytka)) 
            chisloIg = input()
        print(podskazki(chisloIg,secretCif))

        
        popytka += 1

        if chisloIg == secretCif:
            break
        if popytka > KOLPOPITOK:
            print('Попыток больше не осталось. Язагадал число %s.' %(secretCif))
    
    if not again():
        break
# ************************************************************88
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# HBVJVWEJFVJWEVFVWU
import random
# KHBFHHVVVVVIVIVVV
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# VJVJVGVJVJGVVJGVGVVGV
def chotoDrugoe():
    trup = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 0   |
     |
     |
    ===''','''
 +---+
 0   |
 |   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
+---+
 0   |
/|   |
     |
    ===''','''
+---+
 0   |
/|\  |
     |
    ===''','''
+---+
 0   |
/|\  |
/    |
    ===''','''
+---+
 0   |
/|\  |
/ \  |
    ===''']

    return trup

def genZNCH():
    per1 = 'аист акула волк кит паук  агути абия кирилл леново мамонт слон сипуха морж жаворонок шелкопряд барсук бобр белка конь лошадь лис крокодил алигатор маккака попугай жук бабочка ящерица лягушка жаба ворон грач кот собака орёл крыса мышь бабуин хомяк медведь енот волк уж змея ягненок баран козел овца '.split() 
    return per1

def vibor(imya):
    per0 = random.randint(0,len(imya)-1)
    per5 = imya[per0]
    return per5

def prBukvi(per666):
    while True:
        print('Введите букву')
        bukwa = input()
        bukwa = bukwa.lower()
        if len(bukwa) != 1:
            print('Надо ввести только одну букву')
        elif bukwa not in 'абвгдежзийклмнопрстуфхшщьыъэюя':
            print('Надо вводить только русские буквы')
        elif bukwa in per666:
            print('Вы уже называли эту букву')
        else:
            return bukwa

def schinomontasch(viselici,errorBuc,yesBuc,sicretSlovo):
    print(viselici[len(errorBuc)])
    print()
    print('ошибочные буквы: '+errorBuc)
    print()

    per2014 = '_'*len(sicretSlovo)

    for i in range(len(sicretSlovo)):
        if sicretSlovo[i] in yesBuc:
            per2014 = per2014[:i]+sicretSlovo[i]+per2014[i+1:]
   
    for s in per2014:
        print(s,end=' ')
    print()  

def again():    
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


# 8888888888888888888888
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# per2014 = '_'*len(sicretSlovo)

vis = chotoDrugoe()
aboba = genZNCH()
print(aboba[5])
secret = vibor(aboba)
print(secret)

strokaErrS = ''
strokaYesF = ''

while True:
    schinomontasch(vis,strokaErrS,strokaYesF,secret)
    vvedenie = prBukvi(strokaErrS+strokaYesF)


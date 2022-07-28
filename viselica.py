# ************************************************************88
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# HBVJVWEJFVJWEVFVWU
import random
from this import s
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
    per1 = {'животные':'аист акула волк кит паук  агути абия леново мамонт слон сипуха морж жаворонок шелкопряд барсук бобр белка конь лошадь лис крокодил алигатор маккака попугай жук бабочка ящерица лягушка жаба ворон грач кот собака орёл крыса мышь бабуин хомяк медведь енот волк уж змея ягненок баран козел овца '.split(),
'фигуры':'круг квадрат прямоугольник параллелепипед ромб шестиугольник конус куб'.split(),
'овощи':'помидор огурец тыква кабачок лук чеснок редька свекла редиска'.split()}
    return per1

def vibor(slovar,chtoto):
    if chtoto == 'Л':
        for i in range(len(list(slovar.keys()))):
            print('Для выбора категории '+list(slovar.keys())[i]+' введите '+str(i))   

        while True:
            katSl = input()
            if not katSl.isdigit():
                print('введите только цифры')
            else:
                katSl = int(katSl)
                if katSl > len(list(slovar.keys())):
                    print('вы ввели неверное число')
                else:
                    break

        kategoria = list(slovar.keys())[katSl]
    else:
        kategoria = random.choice(list(slovar.keys()))

    indexSl = random.randint(0,len(slovar[kategoria])-1)

    return [slovar[kategoria][indexSl],kategoria]

def viborUs():
    while True:
        print('Выберите уровень сложности:')
        print('Чтобы выбрать легкий уровень сложности введите "Л"')
        print('Чтобы выбрать легкий уровень сложности введите "С"')
        print('Чтобы выбрать легкий уровень сложности введите "Т"')
        lvl = input()
        lvl = lvl.upper()
        if len(lvl) !=1:
            print('Надо вводить только один символ')
        elif lvl not in 'ЛСТ':
            print('Вы ввели неверную букву')
        else:
            return lvl



def prBukvi(per666):
    while True:
        print('Введите букву')
        bukwa = input()
        bukwa = bukwa.lower()
        if len(bukwa) != 1:
            print('Надо ввести только одну букву')
        elif bukwa not in 'абвгдежзийклмнопрстуфхчшщьыъэюя':
            print('Надо вводить только русские буквы')
        elif bukwa in per666:
            print('Вы уже называли эту букву')
        else:
            return bukwa

def schinomontasch(viselici,errorBuc,yesBuc,sicretSlovo,uS,kS):
    if uS in 'ЛС':
        print(kS)
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
        # проверяем ответ на совпадение со следующими фразами
        # "Да","да","д"
        # усли есть совпадение  то переменной присваиваем значение True
        # и прерываем цикл командой return
        if (guess == 'да') or (guess == 'д') or (guess == 'Да'):
            return True
        # проверяем ответ на совпадение со следующими фразами
        # "Нет","нет","н"
        # усли есть совпадение  то переменной присваиваем значение False
        # и прерываем цикл команeдой return
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

levelSl = viborUs()
secret,kategoriaSl = vibor(aboba,levelSl)

strokaErrS = ''
strokaYesF = ''
GO = False

while True:
    schinomontasch(vis,strokaErrS,strokaYesF,secret,levelSl,kategoriaSl)
    vvedenie = prBukvi(strokaErrS+strokaYesF)

    if vvedenie in secret:
        strokaYesF = strokaYesF + vvedenie

        konetsG = True
        for i in range(len(secret)):
            if secret[i] not in strokaYesF:
                konetsG = False
                break
        if konetsG:
            print('ДА! Секретное слово - "'+strokaYesF+'"! Вы угадали! ')
            GO = True
    else:
        strokaErrS = strokaErrS + vvedenie

        if len(strokaErrS)==len(vis)-1:
            schinomontasch(vis,strokaErrS,strokaYesF,secret)
            print('''                           Вы исчерпали все попытки!
        Неугаданно букв: '''+str(len(strokaErrS))+'''
        угаданно букв: '''+str(len(strokaYesF))+'''
        было загаданно слово: '''+secret+'.')
            GO = True
    
    if GO:
        if again():
            levelSl = viborUs()
            secret,kategoriaSl = vibor(aboba,levelSl)

            strokaErrS = ''
            strokaYesF = ''
            GO = False 
        else:
            break
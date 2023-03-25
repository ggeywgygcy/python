# ************************************************************88
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙprint(strOne)print(strOne)(strOne)print(strOne)rint(strOne)print(strOne)int(strOne)
# HBVJVWEJFVJWEVFVWU
import random
import math
import sys

# KHBFHHVVVVVIVIVVV
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# VJVJVGVJVJGVVJGVGVVGV
def razmer():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def dysplay(board):
    strOne = '    '
    for a in range(1,6):
        strOne += (' '*9) + str(a)

    print(strOne)
    print('   '+('0123456789'*6))
    print()

    for row in range(15):
        if row < 10:
            space = ' '
        else:
            space = ''

        boardStr = ''
        for colum in range(60):
            boardStr += board[colum][row]

        print('%s%s %s %s' %(space,row,boardStr,row)) 


    
    print()
    print('   '+('0123456789'*6))
    print(strOne)

def randomSunduki(kolCh):
    sunduk = []
    while len(sunduk)<kolCh:
        newCh = [random.randint(0,59),random.randint(0,14)]
        if newCh not in sunduk:
            sunduk.append(newCh)
    return sunduk



def vopros(samVopros):
       print(samVopros)
       guess = input()
       if (guess == 'да') or (guess == 'д') or (guess == 'Да'):
            return True
       elif (guess == 'нет') or (guess == 'Нет') or (guess == 'н'):
            return False
        # если совпадения с первыми двумя случаями нет
        # говорим пользователю, что не поняли его ответа
       else:
            print('Я не понял ответа')


def OdinHod(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14


def makeMove(boArd,sanduk,x,y):
    miniD = 100
    for cx,cy in sanduk:
        distanciya = math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if distanciya<miniD:
            miniD=distanciya
    miniD = round(miniD)

    if miniD == 0:
        sanduk.remove([x,y])
        print('Вы нашли сундук с сокровищами на затонувшем корабле!!!!!')
        return True
    
    else:
        if miniD<10:
            boArd[x][y] = str(miniD)
            print('Сундук с сокровищами обнаружен на растоянии %s от гидролокатора' % (miniD))
            return False
        
        else:
            boArd[x][y] = 'X'
            print(' Гилролокатори не обнаружил ничего. Сундуки с сокровищами не обнаружены в пределе осягаемости')
            return False


def redaktirovanie(predHoda):
    print('''Где следуетопустить гидролокатор? 
    (координаты 0-59 0-14) 
    (или введите "выход" для прекращения игры)"''')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and OdinHod(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in predHoda:
                print('дезь вы уже опускали гидролокатор')
            else:
                return [int(move[0]),int(move[1])]
        else:
            print('Введите числа от 0 до 59, потом пробел, а потом от 0 до 14')

def pravilaIgri():
    
    print('''Приветствую вас в игре поиск сокровищ!
    В этой игре вы будете в роли капитана корабля искать сундуки
    с сокровищем на дне океана. Всего их 3. Искать вы будете с помощью гидролокаторов, чтобы их опустить
    вы должны написать координаты: от 0-59 в длину, от 0 до 14 в ширину.''')
    
    input('Для прородолжения прочтения правил нажмите на кнопку "Enter"')

    print('''Игровое поле выглядит вот так:
        _0_1_2_3_______________________________
       1|
       2|
       3|           I
        |                           I
        |                       I
        |
        |______________________________________
        *I - это сундуки. (Игровое поле в правилах и игровое поле в самой игре не
        соответствуют друг-другу)''')

    input('Для прородолжения прочтения правил нажмите на кнопку "Enter"')

    print('''Когда вы напишите координату Х, то она будет равна верхним координатам
    (от 0 до 59). Когда вы напишите координату Y, то она будет равна нижним координатам 
    (от 0 до 14).''')

    input('Для прородолжения прочитания правил нажмите на кнопку "Enter"')

    print('''Чтобы опустить гидролокатор вы должны ввести сначала координату Х(от 0 до 59),
    а потом  координату Y(от 0 - 14). Вот как это должно выглядеть на игровом поле:
        _0_1_2_3____7___________________________
       1|          |
       2|          |
       3|_________I           
        |                           I
        |                       I
        |
        |______________________________________
        *I - это сундуки
        координата Х - 7
        координата Y - 3''')

    input('Для прородолжения прочтения правил нажмите на кнопку "Enter"')

    print('''!ЗАПОМНИТЕ!
    Повторно координаты вводить нельзя!
    После того как вы найдете все сундуки вы выйграете, а если
    не найдете то проиграете. 
    ЖЕЛАЮ УДАЧИ!''')

    print('''Вот твое игровое поле в игре:
                     1         2        3
            01234678901234567890123456780912
        
        0 ``~~``~~``~~~```~~~~~``````~````   0
        1 ~~~~``~~~I```~~~```~~~```````~~~`` 1
        2 ~~~~~~~``````~~~~~~~~~`````~~~~~```2
        3 ~~~~~~~~``I~~~`````~~~~~~~~~~~~~~~`3
        4 ```~~~```~~~~~I`````~~~~~````~~~~``4
''')

#############
#Основное тело программы
#############
print('Это игра поиск сокровищ')
print()
if vopros('Хотите прочитать инструктаж?'):
    pravilaIgri()

while True:
    kolLokator = 20
    tHEbOARD = razmer()
    sunduki = randomSunduki(3)
    dysplay(tHEbOARD)
    print()
    predHody = []

    while kolLokator>0:
        # Показать  сколько осталось гидролокаторов и ненайденных сундучков
        

        if len(sunduki)==1:
            okon = ''
        else:
            okon = 'а'
        print('осталось %s неиспользованых гидролокаторов. Необходимо найти еще %s сундук%s.' % (kolLokator,len(sunduki),okon))
        x,y = redaktirovanie(predHody)
        predHody.append([x,y])


        if makeMove(tHEbOARD,sunduki,x,y):
            for x,y in predHody:
                makeMove(tHEbOARD,sunduki,x,y)
        dysplay(tHEbOARD)

        if len(sunduki) == 0:
            print('Вы нашли все сундуки с слкровищами на затонувшем корабле! Поздравляем!')
            break
        kolLokator -= 1

    if kolLokator == 0:
        print('''   Все гидролокаторы опущены на дно!
        Придется разворачивать корабль и отправляется домой, в порт!
        Игра окончена!''')
        print()
        print('     Вы не нашли сундуки в следующих местах:')
        for x,y in sunduki:
            print(' %s, %s' % (x,y))

    if not vopros('Хотите играть ещe?'):
        sys.exit()

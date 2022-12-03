# ************************************************************88
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙprint(strOne)print(strOne)(strOne)print(strOne)rint(strOne)print(strOne)int(strOne)
# HBVJVWEJFVJWEVFVWU
import random
import math

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
    while len(sunduk)<=kolCh:
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

# tcu
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# FF

while True:
    a = int(input('Введите первую координату     '))
    b = int(input('Введите вторую координату     '))
    print(OdinHod(a,b))
    if vopros('Вы хотите прервать проверку?'):
        break




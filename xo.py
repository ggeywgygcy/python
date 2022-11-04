#  Игра "КРЕСТИКИ-НОЛИКИ"

# ппапар
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# hgh
import random
# uju
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ 
# hbhh
def db(h1):
    # эта функция выводит на экран игровое поле
    # клетки корого будут заполнятся

    # "board" - это список в котором хранится 10 строк
    # для прорисовки игрового поля (индекс 0 игнорируется)

    print(h1[7]+'|'+h1[8]+'|' +h1[9])
    print('-+-+-')
    print(h1[4]+'|'+h1[5]+'|' +h1[6])
    print('-+-+-')
    print(h1[1]+'|'+h1[2]+'|' +h1[3])
 
def pl():
    # предложи игрокуввести букву, которую он выбирает
    letter = ''
    while not (letter=='X' or letter=='O'):
        print(''' Выберите Х или О 
     ef kch(   для выбора введите соответственно Х или О
        на англ. раскладке. ''')

        letter = input().upper()

        if letter == 'x':
            return ['X','O']
        else:
            return ['O','X']

def iFS():
    # случайным образом выбираем ктот будет ходить первым
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'
    
def goldexpiriensreqiem(per1,p2,p4):
    per1[p4] = p2

def kaknazvat(bd,lt):
    return ((bd[1] == lt and bd[2] == lt and bd[3] == lt) or 
           (bd[4] == lt and bd[5] == lt and bd[6] == lt) or 
           (bd[7] == lt and bd[8] == lt and bd[9] == lt) or
           (bd[7] == lt and bd[4] == lt and bd[1] == lt)or
           (bd[8] == lt and bd[5] == lt and bd[2] == lt)or
           (bd[9] == lt and bd[6] == lt and bd[3] == lt)or
           (bd[7] == lt and bd[5] == lt and bd[3] == lt)or
           (bd[1] == lt and bd[3] == lt and bd[9] == lt)) 

def gBC(board):
    CB = []
    for i in board:
        CB.append(i)
    return CB

def isFS(b,m):
    return b[m] == ' '

def gPM(boa):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9' .split() or not isFS(boa,int(move)):
        print('Ваш следующий ход? введите номер яйчейки (1-9)')
        move = input()
    return int(move)
           
def cRMN(board2,naklz):
    dragonball = []
    for i in naklz:
        if isFS(board2,i):
            dragonball.append(i)

    if len(dragonball) != 0:
        return random.choice(dragonball)
    else:
        return None

def h1(pc,cl):
    
    if cl == 'X':
        pc = 'O'
    else:
        pc = 'X'
    
    for i in range(1,10):
        boardC = gBC(boardC)

    if gPM(boardC,i):
        kaknazvat(boardC,cl,i)
        
        if goldexpiriensreqiem(boardC,cl):
            return i  
    
    for i in range(1,10):
            boardC = gBC(boardC)
            gPM         
            if goldexpiriensreqiem(boardC,pl):
                return i  

    move = cRMN(boardC,[1,3,7,9])
    if move != None:
        return move

    if iFS(boardC,5):
        return 5

    return cRMN(boardC,[1,3,7,9])

def isBF(board):
    for i in range(1,10):
        if iFS(board,i):
            return False
    return True    










# tcu
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# FF

#fftfty
print('ИГРА КРЕСТИКИ НОЛИКИ888')

while True:
    theBoard = [' ']*10

    pc,cl = h1(pc,cl)

    turn = gPM()
    print(''+turn+' ходит первым.')
    
    while iFS:
        if turn == 'Человек':
            dB(theBoard)
            move = gPM
            kaknazvat(theBoard,pl,move)

            if goldexpiriensreqiem(theBoard,pl):
                dB(theBoard)
                print('Ты выйграл')
                gpm = False
            else:
                if isBF(theBoard):
                    dB(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Компьютер'
        else:
            move = iFS(theBoard,cl)
            db(theBoard,cl,move)

            if isBF(theBoard,cl):
                dB(theBoard)
                db(theBoard,cl,move)

            while iFS:
                if turn == 'Человеек':
                    iFS(theBoard)
                move = gPM
            kaknazvat(theBoard,pc,move)

            if db(theBoard,pl):
                iFS(theBoard)
                print('Компьютер был сильнее')
                gpm = False
            else:
                if isBF(theBoard):
                    db(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'
                

            if isBF(theBoard,cl):
                iFS(theBoard)
                db(theBoard,cl,move)
            else:    
                    move = iFS(theBoard,cl)
                    db(theBoard,cl,move)
            
            print('Сыграем ещё раз? (да или нет)')
            if not input.lower().start('д'):
                break
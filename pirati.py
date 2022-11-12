# ************************************************************88
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙprint(strOne)print(strOne)(strOne)print(strOne)rint(strOne)print(strOne)int(strOne)
# HBVJVWEJFVJWEVFVWU
import random
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



# tcu
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# FF

theBoard = razmer()
dysplay(theBoard)





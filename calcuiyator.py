print('''ноль в качестве знака операций
Ctri+Z завершит работу программы''')
while True:
    s = input("Знак (+,-,/,*): ")
    if s == '0':
        break
    if s in('+','-','/','*'):
        a = float(input("a="))
        b = float(input("b="))
        if s == '-':
            print("%.2f" % (a - b))
        elif s == '+':
            print("%.2f" % (a + b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Делить на ноль нельзя!")
    else:
        print('Неверный знак операции!')
        

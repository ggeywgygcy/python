alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Выберете шаг шифровки: '))
message = input("Слова для шифра: ").upper()
itog = ''
lang = input('Выберите язык RU или EU: ')
if lang == 'RU':
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit:
            itog += alfavit[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit2.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit2:
            itog += alfavit2[new_mesto]
        else:
            itog += i
print (itog) 
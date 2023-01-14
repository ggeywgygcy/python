#jhhh
SYBOLS = 'АБВГДЕЖЗКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдежзийклмнопрстуфхцчшщьыъэюя'
MAX_KEY_SIZE = len(SYBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст?')
        mode = input().lower()
        if mode in ['зашифровать','з','расшифровать','р']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки или "h ')

def getMessage():
    print('Введите текст: ')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key>=1 and key<=MAX_KEY_SIZE):
            return key
    

def getTranslatedMessage(mode,message,key):
    if mode[0] == 'р':
        key = -key 

    translate = ''

    for symbol in message:
        simbolIndex = SYBOLS.find(symbol)
        if simbolIndex == -1:
            # bb
            translate += symbol
        else:
            simbolIndex += key

            if simbolIndex >= len(SYBOLS):
                simbolIndex -= len(SYBOLS)
            elif simbolIndex < 0:
                simbolIndex += len(SYBOLS)

            translate += SYBOLS[simbolIndex]
    return translate

mode = getMode()
message = getMessage()
key = getKey()

print('Преобразованный текст:')
print(getTranslatedMessage(mode,message,key))





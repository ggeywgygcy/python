# game holodno goryacho

#ffurefcfe
# РАЗДЕЛ ИМПОРТА НОЛЕЙ
#HGHUTHGU
import random
#hfuiogi5gifgifgiyg5
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# V4EVRYIFIYVE

KOLCHISEL = 3
KOLPOPITOK = 15

def generaciya():
    cifri = list(range(10))
    random.shuffle(cifri)
    sicretCif = ''
    for a in range(KOLCHISEL):
        sicretCif += str(cifri[a])
    return sicretCif

#goerogoutg
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#EHGOUREUHGIG

print(generaciya())



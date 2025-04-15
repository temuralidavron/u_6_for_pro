import random

son=random.randint(1,5)

while True:
    user=int(input('sonni txmin qilng(1,5)'))
    if user==0:
        break
    if user==son:
        print('topdingiz')
        break
    else:
        print('topolmadingiz')

import random
*l,=range(1,10001)
random.shuffle(l)
for i in l:
    print('? A',i)
    if int(input()):
        A=i;break
for i in l:
    print('? B',i)
    if int(input()):
        B=i;break
print('!',A+B)
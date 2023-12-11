import random
*l,=range(1,10001)
random.shuffle(l)
i=0
while 1:
    print('? A',l[i:=i+1])
    if int(input()):
        A=l[i];break
i=0
while 1:
    print('? B',l[i:=i+1])
    if int(input()):
        B=l[i];break
print('!',A+B)
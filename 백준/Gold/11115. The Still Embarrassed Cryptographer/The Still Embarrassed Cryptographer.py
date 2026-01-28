import math
for _ in[0]*int(input()):
    s1=input()
    s2=input()
    trans=s1.maketrans(s1,s2)
    for i in range(2310):
        if s1==s2:
            print(i)
            break
        else:
            s2=s2.translate(trans)
    else:
        print('mjau')
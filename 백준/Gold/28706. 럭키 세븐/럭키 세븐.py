import sys
input=sys.stdin.readline
for _ in range(int(input())):
    K=[0,1,0,0,0,0,0]
    for _ in range(int(input())):
        tmp=[0]*7
        a,b,c,d=input().split()
        if a=='+':
            for i in range(7):
                tmp[(i+int(b))%7]=max(tmp[(i+int(b))%7],K[i])
        if a=='*':
            for i in range(7):
                tmp[i*int(b)%7]=max(tmp[i*int(b)%7],K[i])
        if c=='+':
            for i in range(7):
                tmp[(i+int(d))%7]=max(tmp[(i+int(d))%7],K[i])
        if c=='*':
            for i in range(7):
                tmp[i*int(d)%7]=max(tmp[i*int(d)%7],K[i])
        K=tmp
    if K[0]:print('LUCKY')
    else:print('UNLUCKY')
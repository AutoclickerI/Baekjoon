import sys
s=0
x=0
for i in[0]*int(input()):
    a=list(map(int,sys.stdin.readline().split()))
    if a[0]==1:
        s+=a[1]
        x^=a[1]
    elif a[0]==2:
        s-=a[1]
        x^=a[1]
    elif a[0]==3:
        print(s)
    elif a[0]==4:
        print(x)
import sys
input=sys.stdin.readline
b=0
i=a=1
for _ in[0]*int(input()):
    *l,=map(int,input().split())
    if len(l)-2:
        print(i*a+b)
    else:
        p,q=l
        if 0==p:b+=q
        if p==1:a*=q;b*=q
        if p==2:i+=q
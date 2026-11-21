import sys
input=sys.stdin.readline
n=int(input())
*l,=map(int,input().split())
for _ in[0]*int(input()):
    p,q,r=map(int,input().split())
    if p-1:
        print(sum(l[q-1:r]))
    else:
        for i in range(q-1,r):
            l[i]=l[i]**2%2010
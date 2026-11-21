import sys
input=sys.stdin.readline
p,q=map(int,input().split())
l=[0]*p
a=0
i=0
while i<len(l):
    l[i]=1
    i+=10
    a+=1
i=3
while i<len(l):
    l[i]=1
    i+=10
    a+=1
i=6
while i<len(l):
    l[i]=1
    i+=10
    a+=1
for _ in[0]*q:
    n=int(input())-1
    if l[n]:l[n]=0;a-=1
    else:l[n]=1;a+=1
    print(a)
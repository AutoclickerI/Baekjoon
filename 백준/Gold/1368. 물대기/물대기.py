def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

N=int(input())
*p,=range(N+1)
e=[]
for i in range(N):
    e+=(int(input()),0,i+1),
for i in range(N):
    for j,v in enumerate(map(int,input().split())):
        if i!=j:
            e+=(v,i+1,j+1),
e.sort()
r=0
for v,i,j in e:
    i,j=sorted(map(find,[i,j]))
    if i-j:
        r+=v
        p[j]=i
print(r)
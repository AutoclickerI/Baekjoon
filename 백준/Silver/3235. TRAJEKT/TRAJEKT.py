def fOrd(x):
  a,b=map(int,x.split(':'))
  return a*60+b

import sys
I=sys.stdin.readline
MI=lambda:map(int,I().split())

u,v=MI();u+=v
n=int(I())
A=[(fOrd(I()),0) for _ in' '*n]
m=int(I())
A.extend([(fOrd(I()),1) for _ in' '*m])
A.sort()
n+=m;r=0
V=[1]*n
for i in range(n):
  if not V[i]:continue
  r+=1;V[i]=0;a,f=A[i];a+=u
  while 1:
    for j in range(i+1,n):
      if A[j][0]<a or not V[j] or f==A[j][1]:continue
      V[j]=0;a=A[j][0]+u;f^=1
      break
    else:break
print(r)
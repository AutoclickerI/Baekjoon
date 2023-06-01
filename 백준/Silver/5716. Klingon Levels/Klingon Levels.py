from bisect import *
while True:
 n=int(input())
 if n==0:break
 l=[]
 for _ in range(n):
  input()
  l.append(sorted(list(map(int,input().split()))))
 MIN=10**9
 for i in range(1001):
  s=0
  for k in range(n):
   s+=abs(len(l[k])-2*bisect_left(l[k],i))
  if MIN>s:MIN=s
 print(MIN)
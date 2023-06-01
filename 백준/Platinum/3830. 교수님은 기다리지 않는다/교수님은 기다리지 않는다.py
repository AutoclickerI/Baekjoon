import sys
sys.setrecursionlimit(9**9)
I=sys.stdin.readline
while ord((s:=I())[0])-48:
 p,q=map(int,s.split());P=[*range(p+1)];d=[0]*(p+1)
 def F(n):
  if P[n]-n:p=F(P[n]);d[n]+=d[P[n]];P[n]=p;return p
  return n
 for _ in[0]*q:
  Q,*l=I().split()
  if Q=='!':
   a,b,w=map(int,l);A=F(a);B=F(b)
   if A-B:d[B]=d[a]-d[b]+w;P[B]=A
  else:a,b=map(int,l);print('UNKNOWN'*(F(a)!=F(b))or d[b]-d[a])
import sys
sys.setrecursionlimit(9**9)
I=sys.stdin.readline
while'0'!=(s:=I())[0]:
 p,q=map(int,s.split());P=[*range(p+1)];d=[0]*(p+1)
 def F(n):
  if P[n]-n:p=F(P[n]);d[n]+=d[P[n]];P[n]=p;return p
  return n
 for _ in[0]*q:
  Q,*l=I().split();k=map(int,l)
  if Q=='!':
   a,b,w=k;A=F(a);B=F(b)
   if A-B:d[B]=d[a]-d[b]+w;P[B]=A
  else:a,b=k;print('UNKNOWN'*(F(a)!=F(b))or d[b]-d[a])
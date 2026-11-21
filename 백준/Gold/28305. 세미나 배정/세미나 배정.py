N,T,*l=map(int,open(s:=0).read().split())
l.sort()
def P(n):
 S=[0]*n
 for i in range(N):
  if l[i]<=S[i%n]:return 1
  S[i%n]=max(S[i%n]+T,l[i])
e=N
while e-s>1:
 if P(m:=(s+e)//2):s=m
 else:e=m
print(e)
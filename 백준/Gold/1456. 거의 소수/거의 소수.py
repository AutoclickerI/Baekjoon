A,B=map(int,input().split())
M=6**9
P=[1]*M
z=0
for p in range(2,M):
 if P[p]:
  k=p*p;P[k::p]=(M+p+~k)//p*[0]
  while k<=B:z+=A<=k;k*=p
print(z)
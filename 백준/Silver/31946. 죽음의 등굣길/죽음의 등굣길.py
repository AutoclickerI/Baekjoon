k='DEAD'
n,m,*l,x=map(int,open(0).read().split())
q=[0]
c=l[0]
for i in q:
 if-~i==n*m:k='ALIVE'
 for j in range(n*m):
  if(abs(i//m-j//m)+abs(i%m-j%m)<=x)*(c==l[j]):l[j]^=1;q+=j,
print(k)
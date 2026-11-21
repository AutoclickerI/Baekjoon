N,*l=map(int,open(0).read().split())
D=[0]*N
for i in l[N:]:
 c=0
 for j in range(N):
  if i==l[j]:D[j]=c+1
  elif i>l[j]:c=max(c,D[j])
print(max(D))
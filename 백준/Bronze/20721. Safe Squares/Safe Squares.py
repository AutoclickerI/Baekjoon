r=[1]*8
c=r[:]
for i in range(8):
 for j,x in enumerate(input()):
  if'.'<x:r[i]=c[j]=0
print(sum(r)*sum(c))
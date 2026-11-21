_,*b=open(m:=0,'rb')
l=[[i%2 for i in b[0]]]
r=l[:]
for i in b[1:]:l+=[p%2*-~q for p,q in zip(i,[0]+l[-1])],;r+=[p%2*-~q for p,q in zip(i,r[-1][1:]+[0])],
R=range
for y in R(len(b)):
 for x in R(len(b[0])):
  for t in R(m,k:=min(l[y][x],r[y][x])):m=max(m,-~t*(r[y-t][x-t]>t<l[y-t][x+t]))
print(m)
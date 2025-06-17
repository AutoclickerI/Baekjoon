n,x=map(int,input().split())
d=[*map(int,input().split())]
s=m=1
for i,j in zip(d,d[1:]):
  if j-i<=x:s+=1
  else:s=1
  m=max(m,s)
print(max(m,s))
T=[0,15,19,28,38,41,53,58]
n,a=open(0)
r=''
for i in range(int(n)):
 for j in T:
  c=0;x=int(a[i*6:i*6+6],2)^j
  if x in(0,x&-x):r+=chr(65+T.index(j));break
 else:r=i+1;break
print(r)
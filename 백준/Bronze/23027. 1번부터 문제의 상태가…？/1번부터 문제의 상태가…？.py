s=input()
f='A'*len(s)
for i in'ABC':
 if~s.find(i):
  for j in'ABCDF':f=s=s.replace(j,i)
print(f)
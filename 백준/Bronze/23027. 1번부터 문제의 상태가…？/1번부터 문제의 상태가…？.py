f='A'*len(s:=input())
for i in'ABC':
 if i in s:
  for j in'ABCDF':f=s=s.replace(j,i)
print(f)
n,a=open(t:=0)
s=''
for i in a:
 t|=1<<'RGB\n'.find(i)
 if t==7:t=0;s+=i
print(s[:int(n)])
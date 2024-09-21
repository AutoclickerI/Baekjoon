n,v,*l=open(c:=0)
v=int(v[-3:])
for i in l:v+=int(i[-3:]);c+=v%100and 1
print(c)
n,v,*l=open(c:=0)
v=int(v[-3:])
for i in l:v+=int(i[-3:]);c+=0<v%100
print(c)
n,v,*l=open(0)
v=int(v[-3:])
print(sum(0<(v:=v+int(i[-3:]))%100for i in l))
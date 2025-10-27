v,*l=map(int,[*open(0)][1].split())
s=m=v
for i in l:v,s=v*(0<v)+i,max(v,s+i);m=max(m,v,s)
print(m)
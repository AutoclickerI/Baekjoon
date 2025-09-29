for i in[*open(v:=0)][1:]:s,e=map(int,i.split());v+=e-s-(0<e)+(0<s)
if-1<v:v+=1
print(v)
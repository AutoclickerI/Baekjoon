for i in[*open(v:=0)][1:]:s,e=map(int,i.split());v+=e-s-(0<e)+(0<s)
print(v+(-1<v))
v,*z=2000,
L=[v]*v
for i in[*open(c:=0)][2:]:s,e=map(int,i.split());L[s:e+1]=map(min,L[s:e+1],[c:=c+1]*v);z+=(s-e,c),
print(min(z)[1],max(range(v),key=L.count))
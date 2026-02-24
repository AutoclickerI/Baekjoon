a=-1e9
for i in[*open(s:=0)][1:]:
 x,y=map(int,i.split())
 if a<y:s+=y-max(x,a);a=y
print(s)
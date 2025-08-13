d={}
for i in[*open(a:=0)][1:]:a+=d.get(v:=i[:-2],i)!=i;d[v]=i
print(a)
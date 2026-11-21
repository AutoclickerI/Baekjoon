d={}
for i in[*open(0)][1:]:d[i]=d.get(i,0)+1
print(['NONE',s:=max(d,key=d.get)][2*d[s]>sum(d.values())])
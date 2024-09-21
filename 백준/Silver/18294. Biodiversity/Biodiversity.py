d={}
for i in[*open(0)][1:]:d[i]=d.get(i,0)+1
s=max(d,key=d.get)
print(['NONE',s][2*d[s]>sum(d.values())])
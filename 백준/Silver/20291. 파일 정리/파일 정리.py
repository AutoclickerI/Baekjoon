d={}
for i in[*open(0)][1:]:_,v=i[:-1].split('.');d[v]=d.get(v,0)+1
for i in sorted(d):print(i,d[i])
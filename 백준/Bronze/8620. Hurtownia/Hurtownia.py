d={}
for i in[*open(0)][1:]:s,v=i.split();d[s]=d.get(s,0)+int(v)
for i in sorted(d):print(i,d[i])
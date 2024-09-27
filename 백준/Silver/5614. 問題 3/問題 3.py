d={}
for i in[*open(0)][1:]:p,c=i.split();d[p]=d.get(p,0)+int(c)
for i in sorted(d,key=lambda x:(len(x),x)):print(i,d[i])
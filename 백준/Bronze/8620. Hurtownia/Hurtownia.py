d={}
for i in[*open(0)][1:]:d[i[0]]=d.get(i[0],0)+int(i[1:])
for i in sorted(d):print(i,d[i])
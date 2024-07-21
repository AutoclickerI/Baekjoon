d={}
for i in[*open(0)][1].split():d[i]=d.get(i,-1)+1
print(sum(d.values()))
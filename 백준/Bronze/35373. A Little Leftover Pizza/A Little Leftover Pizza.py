d={}
for i in[*open(0)][1:]:
    p,n=i.split()
    d[p]=d.get(p,0)+int(n)
print(-sum(d.get(i,0)//-j for i,j in[('S',6),('M',8),('L',12)]))
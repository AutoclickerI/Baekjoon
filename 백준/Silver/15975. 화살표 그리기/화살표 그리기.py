d={}
for i in[*open(0)][1:]:
    n,c=map(int,i.split())
    d[c]=d.get(c,[])
    d[c]+=n,
r=0
for i in d:
    d[i].sort()
    if 1<len(d[i]):
        r+=d[i][1]-d[i][0]+d[i][-1]-d[i][-2]
        r+=sum(min(l-k,k-j)for j,k,l in zip(d[i],d[i][1:],d[i][2:]))
print(r)
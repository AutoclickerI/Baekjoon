d={}
for i in[*open(0)][1:]:
    x,y=map(int,i.split())
    d[y]=d.get(y,[])
    d[y]+=x,

r=0
for i in d:
    i=-1e9,*sorted(d[i]),1e9
    r+=sum(min(j-i,k-j)for i,j,k in zip(i,i[1:],i[2:]))
print(r)
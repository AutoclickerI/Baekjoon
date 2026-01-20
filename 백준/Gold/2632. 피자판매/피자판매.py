v,n,m,*l=map(int,open(0).read().split())
def getper(n,arr):
    p=[0]
    for i in arr:p+=p[-1]+i,
    sa=sum(arr)
    d={sa:1,0:1}
    for s in range(1,n):
        for e in range(s,n):
            v=p[e+1]-p[s]
            d[v]=d.get(v,0)+1
            d[sa-v]=d.get(sa-v,0)+1
    return d
da=getper(n,l[:n])
db=getper(m,l[n:])
c=0
for i in da:
    c+=da[i]*db.get(v-i,0)
print(c)
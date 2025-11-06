N,K,*a=map(int,open(0).read().split())
d={}
c=p=m=0
for i in a:
    c+=1
    d[i]=d.get(i,0)+1
    while K<d[i]:
        c-=1
        d[a[p]]-=1
        p+=1
    m=max(c,m)
print(m)
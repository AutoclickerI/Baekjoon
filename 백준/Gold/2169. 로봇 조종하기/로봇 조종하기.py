[N,M],i,*b=[[*map(int,i.split())]for i in open(0)]
v=0
l=[v:=v+c for c in i]
for i in b:
    rr=[-float('inf')]*M
    ll=rr[:]
    for c in range(M):
        rr[c]=max(l[c],rr[c-1])+i[c]
        ll[~c]=max(l[~c],ll[~c+1])+i[~c]
    *l,=map(max,rr,ll)
print(l[-1])
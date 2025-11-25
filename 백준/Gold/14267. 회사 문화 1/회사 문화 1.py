[n,m],p,*l=[map(int,i.split())for i in open(0)]

edges=[[]for _ in[0]*-~n]
i=0
for c in p:
    i+=1
    if 0<c:
        edges[c]+=i,
                
v=[0]*-~n
for i,c in l[:m]:v[i]+=c

l=[(0,1)]
r=[0]*-~n
for a,n in l:
    a+=v[n]
    r[n]=a
    for e in edges[n]:
        l+=(a,e),
print(*r[1:])
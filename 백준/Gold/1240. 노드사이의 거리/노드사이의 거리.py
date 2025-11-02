[N,M],*l=[[*map(int,i.split())]for i in open(0)]
edges=[[]for _ in[0]*-~N]
for s,e,n in l[:N-1]:edges[s]+=(e,n),;edges[e]+=(s,n),
for s,e in l[N-1:]:
    v=[0]*-~N
    v[s]=1
    z=[(0,s)]
    for c,n in z:
        if n==e:print(c);break
        for b,x in edges[n]:
            if v[b]<1:
                z+=(c+x,b),
                v[b]=1
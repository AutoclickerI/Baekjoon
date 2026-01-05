[N,K,M],*l=[[*map(int,i.split())]for i in open(0)]
ref=[[]for _ in[0]*-~N]
vv=[]
c=0
for i in l:
    vv+=i,
    for v in vv[-1]:
        ref[v]+=c,
    c+=1

v=[float('inf')]*-~N
v[1]=1
l=[(1,1)]
for n,c in l:
    for rr in ref[n]:
        for e in vv[rr]:
            if c+1<v[e]:
                v[e]=c+1
                l+=(e,c+1),
print(-(v[-1]==float('inf'))or v[-1])
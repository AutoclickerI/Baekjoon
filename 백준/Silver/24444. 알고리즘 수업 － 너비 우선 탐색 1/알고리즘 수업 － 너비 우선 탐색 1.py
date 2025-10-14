[N,M,R],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~N]

for s,e in l:
    edges[s]+=e,
    edges[e]+=s,

l=[R]
v=[0]*-~N
v[R]=1
cnts=[0]*-~N
cnt=0
for i in l:
    cnt+=1
    cnts[i]=cnt
    for e in sorted(edges[i]):
        if v[e]<1:
            v[e]=1
            l+=e,
print(*cnts[1:])
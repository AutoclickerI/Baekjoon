[N,M,X],*l=[map(int,i.split())for i in open(0)]
    
fwd=[[]for _ in[0]*-~N]
bwd=[[]for _ in[0]*-~N]

for s,e in l:
    fwd[s]+=e,
    bwd[e]+=s,

f=[X]
fv=[0]*-~N
for n in f:
    for e in fwd[n]:
        if fv[e]<1:
            fv[e]=1
            f+=e,

b=[X]
bv=[0]*-~N
for n in b:
    for e in bwd[n]:
        if bv[e]<1:
            bv[e]=1
            b+=e,

f=sum(fv)
b=sum(bv)

print(b+1,N-f)
N,K=map(int,input().split())
vo=[float('inf')]*500001
vz=vo[:]

l=[(0,N)]
vz[N]=0

for t,n in l:
    if t%2:
        vv=vz
    else:
        vv=vo
    for e in n-1,n+1,n*2:
        if 0<=e<500001 and t+1<vv[e]:
            vv[e]=t+1
            l+=(t+1,e),

i=0
mv=float('inf')
while K<500001:
    if ~i%2:
        if vz[K]<=i:
            mv=min(mv,i)
    else:
        if vo[K]<=i:
            mv=min(mv,i)
    i+=1
    K+=i
print(-(mv==float('inf'))or mv)
K,N,*p=map(int,open(0).read().split())
from heapq import*

hq=[1]
hq_m=[]
v={}
u={}
cnt=0
mv=float('inf')
for _ in[0]*-~N:
    n=heappop(hq)
    for i in p:
        if i*n not in v and i*n<mv:
            cnt+=1
            heappush(hq,i*n)
            v[i*n]=cnt
            heappush(hq_m,-i*n)
    while N<len(hq_m):
        mv=min(mv,-heappop(hq_m))
        
print(n)
from heapq import*
[N,k],*l=[[*map(int,i.split())]for i in open(0)]
hq=[(0,i+1)for i in range(k)]
p=[]
r=[]
pv=0
for i,w in l:
    v,pos,*ix=heappop(hq)
    if v!=pv:
        pv=v
        r+=p[::-1]
        p=[]
    p+=ix
    heappush(hq,(v+w,pos,i))
while hq:
    v,pos,*ix=heappop(hq)
    if v!=pv:
        pv=v
        r+=p[::-1]
        p=[]
    p+=ix
print(sum(i*v for i,v in enumerate(r+p[::-1],1)))
l=sorted([i.split()for i in open(0)][1:])

from heapq import*
hq=[]

mv=cnt=0

for idx,(s,e) in enumerate(l):
    heappush(hq,(s,'0',1,idx))
    heappush(hq,(e,'1',-1,idx))

while hq:
    n,_,v,idx=heappop(hq)
    cnt+=v
    if mv<cnt:
        mv=cnt
        a=n
print(a)
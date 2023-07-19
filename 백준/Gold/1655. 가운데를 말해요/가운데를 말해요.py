from heapq import*
N,hl,*l=map(int,open(0))
hh=[]
print(hl)
hl=[-hl]
for v in l:
    if -hl[0]>v:
        heappush(hl,-v)
    else:
        heappush(hh,v)
    while len(hl)-len(hh)>1:
        heappush(hh,-heappop(hl))
    while len(hh)-len(hl)>0:
        heappush(hl,-heappop(hh))
    print(-hl[0])
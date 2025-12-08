hq=[]
from heapq import*

for i in[*open(0)][1:]:
    if i<'1':
        if hq:
            print(-heappop(hq))
        else:
            print(-1)
    else:
        for c in i.split()[1:]:
            heappush(hq,-int(c))
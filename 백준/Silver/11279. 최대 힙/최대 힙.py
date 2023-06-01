from heapq import*
h=[]
for i in[*map(int,open(0))][1:]:
    if i:heappush(h,-i)
    else:print(-heappop(h)if h else 0)
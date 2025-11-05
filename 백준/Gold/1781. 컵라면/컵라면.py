from heapq import*
h=[]
for d,v in sorted([[*map(int,i.split())]for i in open(0)][1:]):
 heappush(h,v)
 while d<len(h):heappop(h)
print(sum(h))
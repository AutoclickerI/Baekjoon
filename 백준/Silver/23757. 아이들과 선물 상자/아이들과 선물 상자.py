from heapq import*
_,v,w=[map(int,i.split())for i in open(0)]
h=sorted(-i for i in v)
print(+all(heappush(h,v:=heappop(h)+i)!=v<1for i in w))
from heapq import*
_,*l=map(int,open(s:=0))
heapify(l)
while 1<len(l):
    a=heappop(l)
    b=heappop(l)
    s+=a+b
    heappush(l,a+b)
print(s)
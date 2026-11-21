from heapq import*
O=heappop
_,*l=map(int,open(s:=0))
l.sort()
while~-len(l):heappush(l,t:=O(l)+O(l));s+=t
print(s)
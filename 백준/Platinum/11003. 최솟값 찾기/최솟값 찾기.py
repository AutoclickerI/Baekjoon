N,L=map(int,input().split())
l=[(i,idx)for idx,i in enumerate(map(int,input().split()))]

from heapq import*

hq=[]

a=[]

for i in range(N):
    heappush(hq,l[i])
    while L<=i-hq[0][1]:heappop(hq)
    a+=hq[0][0],

print(*a)
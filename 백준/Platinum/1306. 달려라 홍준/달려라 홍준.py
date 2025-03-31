N,M=map(int,input().split())
l=[[-i,0]for i in map(int,input().split())]+[[1e9,0]]

from heapq import*

hq=l[:2*M-1]

heapify(hq)

a=[]

for i in range(N-2*M+2):
    while hq[0][1]:heappop(hq)
    a+=-hq[0][0],
    l[i][1]=1
    heappush(hq,l[i+2*M-1])

print(*a)
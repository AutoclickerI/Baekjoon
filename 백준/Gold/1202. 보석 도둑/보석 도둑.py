N,K=map(int,input().split())

l=sorted([*map(int,input().split())]for _ in[0]*N)[::-1]

b=sorted([int(input())for _ in[0]*K])

from heapq import*

hq=[]
a=0

for i in b:
    while l and l[-1][0]<=i:
        heappush(hq,-l.pop()[1])
    if hq:a-=heappop(hq)

print(a)
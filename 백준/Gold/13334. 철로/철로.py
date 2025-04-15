import sys
input=sys.stdin.readline

N=int(input())

l=[sorted(map(int,input().split()))for _ in[0]*N]

L=int(input())

from heapq import*

ans=cnt=0

hq=[]

for s,e in l:
    if e<=s+L:
        heappush(hq,(e-L,1))
        heappush(hq,(s+1,-1))

while hq:
    cnt+=heappop(hq)[1]
    ans=max(ans,cnt)

print(ans)
import sys

input=sys.stdin.readline

N,Q=map(int,input().split())
hq=[]
z=0
mv=1e18
for i in map(int,input().split()):
    if i<1:z+=1
    else:hq+=i,;mv=min(mv,i)

from heapq import*

heapify(hq)

for _ in range(Q):
    x,y=map(int,input().split())
    if y==1:
        continue
    tmp=[]
    while hq and hq[0]<=x:
        tmp+=heappop(hq),
    
    for i in tmp:
        if y==0:
            z+=1
        else:
            heappush(hq,i*y)

print(*'0'*z,*sorted(hq))
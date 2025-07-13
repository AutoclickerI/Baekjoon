import sys
input=sys.stdin.readline

from heapq import*

hq=[]
N,H=map(int,input().split())

for _ in range(N):
    s,e=map(int,input().split())
    heappush(hq,(s,1))
    heappush(hq,(e,-1))

f=0
duration=[]
t=s=0

while hq:
    t,v=heappop(hq)
    f+=v
    if f==v:
        duration+=t-s-1,
    if f==0:
        s=t
duration+=H-t,

duration.sort()

a=[sum(duration)]

for i in duration[:-1]:
    a+=a[-1]-i,

from bisect import*

for _ in range(int(input())):
    i=int(input())
    idx=bisect_left(duration,i)
    if idx==len(a):
        print(0)
    else:
        print(a[idx]-(i-1)*(len(duration)-idx))
n=int(input())
*a,=map(int,input().split())
*b,=map(int,input().split())
t=[float('inf')]*n

from heapq import*

hq=[]

for i in range(n):
    if i-a[i]<0 or n<=i+a[i]:
        t[i]=b[i]
        heappush(hq,(b[i],i))

dst=[[]for _ in[0]*n]

for i in range(n):
    if t[i]==float('inf'):
        dst[i+a[i]]+=i,
        dst[i-a[i]]+=i,
        
while hq:
    c,s=heappop(hq)
    if t[s]<c:
        continue
    for e in dst[s]:
        if c+b[e]<t[e]:
            t[e]=c+b[e]
            heappush(hq,(t[e],e))

print(*t)
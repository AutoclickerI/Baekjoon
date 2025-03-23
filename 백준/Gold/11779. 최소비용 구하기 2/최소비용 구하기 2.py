import sys
#input=sys.stdin.readline

N=int(input())
M=int(input())

edges=[[]for _ in[0]*-~N]

for _ in[0]*M:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),

v=[(9**9,-1)]*-~N

s,e=map(int,input().split())

from heapq import*

hq=[(0,s)]
v[s]=0,0

while hq:
    c,n=heappop(hq)
    if n==e:
        break
    if v[n][0]<c:
        continue
    for ne,nc in edges[n]:
        nc+=c
        if nc<v[ne][0]:
            v[ne]=nc,n
            heappush(hq,(nc,ne))

print(v[e][0])

a=[]

while e:
    a+=e,
    e=v[e][1]

print(len(a))
print(*a[::-1])
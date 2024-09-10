N,M=map(int,input().split())
edge=[[]for _ in[0]*-~N]
for _ in[0]*M:
    a,b,c=map(int,input().split())
    edge[a]+=(b,c),
    edge[b]+=(a,c),

c=[(float('inf'),-1,-1)]*-~N
v=[0]*-~N
v[1]=1
c[1]=(0,-1)
from heapq import heappush,heappop
hq=[(0,1)]

while not v[-1]:
    cost,node=heappop(hq)
    v[node]=1
    if c[node][0]<cost:
        continue
    for end,value in edge[node]:
        if cost+value<c[end][0]:
            c[end]=(cost+value,node,value)
            heappush(hq,(cost+value,end))

not_allowed=[]
track=N
while track>1:
    track_next=c[track][1]
    cost=c[track][2]
    not_allowed+=(track,track_next,cost),(track_next,track,cost)
    track=track_next
not_allowed={*not_allowed}

c=[(float('inf'),-1)]*-~N
v=[0]*-~N
v[1]=1
c[1]=(0,-1)
hq=[(0,1)]

while not v[-1]:
    cost,node=heappop(hq)
    v[node]=1
    if c[node][0]<cost:
        continue
    for end,value in edge[node]:
        if cost+value<c[end][0]and (node,end,value)not in not_allowed:
            c[end]=(cost+value,node)
            heappush(hq,(cost+value,end))
print(c[-1][0])
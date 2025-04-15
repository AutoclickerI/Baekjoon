N=int(input())
*l,=[[*map(int,input().split())]for _ in[0]*N]
c=[[((l[e][0]-l[s][0])**2+(l[e][1]-l[s][1])**2)**.5 for e in range(N)]for s in range(N)]

from heapq import*

state_max=1<<N

v=[state_max*[float('inf')]for _ in[0]*N]

v[0][state_max-1&-2]=0
hq=[(0,state_max-1&-2,0)]

while hq:
    cost,state,current=heappop(hq)
    if v[current][state]<cost:
        continue
    f=state
    while f:
        last=f&-f
        f^=last
        next_node=last.bit_length()-1
        nc=c[current][next_node]+cost
        if nc<v[next_node][state^last]:
            v[next_node][state^last]=nc
            heappush(hq,(nc,state^last,next_node))

print(min(v[i][0]+c[i][0]for i in range(1,N)))
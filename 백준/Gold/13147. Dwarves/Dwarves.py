import sys
input=sys.stdin.readline

from collections import deque

edges={}
deg={}

for _ in[0]*int(input()):
    s,q,e=input().split()
    if q=='>':
        s,e=e,s
    
    deg[e]=deg.get(e,0)+1
    edges[s]=edges.get(s,[])
    edges[s]+=e,

dq=deque()

for i in edges:
    if deg.get(i,0)<1:dq+=i,

a=[]

while dq:
    n=dq.popleft()
    a+=n,
    for e in edges.get(n,[]):
        deg[e]-=1
        if deg[e]<1:
            dq+=e,

print('im'*(len(a)<len({*edges,*deg}))+'possible')
from fractions import Fraction
N,M=map(int,input().split())

s=input()

cnt=0
d={}

def get(v):
    global cnt
    if v in d:
        return d[v]
    ret=d[v]=cnt
    cnt+=1
    return ret

root=get(s)

data=[input().split()for _ in[0]*N]

tobeking=[input()for _ in[0]*M]

for i in data:
    for j in i:
        get(j)
for k in tobeking:
    get(k)

edges=[[]for _ in[0]*len(d)]
v=[Fraction(0,1)]*len(d)
deg=[0]*len(d)

for i,j,k in data:
    deg[get(i)]+=2
    edges[get(j)]+=get(i),
    edges[get(k)]+=get(i),

v[0]=Fraction(1,1)

from collections import deque

dq=deque()
for i in range(len(d)):
    if deg[i]<1:dq+=i,

while dq:
    n=dq.popleft()
    for e in edges[n]:
        v[e]+=v[n]/2
        deg[e]-=1
        if deg[e]<1:
            dq+=e,

print(max(tobeking,key=lambda s:v[get(s)]))
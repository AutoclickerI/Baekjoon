import sys
input=sys.stdin.readline

from fractions import Fraction
N=int(input())

edges=[[]for _ in[0]*-~N]
deg=[0]*-~N
c=[0]*-~N

for _ in[0]*~-N:
    s,e=map(int,input().split())
    edges[s]+=e,
    deg[e]+=1

deg_o=deg[:]

from collections import deque

dq=deque()
cnt=0

for i in range(1,N+1):
    if deg[i]<1:dq+=i,;c[i]=Fraction(1,1);cnt+=1

a=[]

while dq:
    n=dq.popleft()
    if c[n]==cnt and deg_o[n]:
        a+=n,
    for e in edges[n]:
        deg[e]-=1
        c[e]+=c[n]/len(edges[n])
        if deg[e]<1:
            dq+=e,

print(*a)
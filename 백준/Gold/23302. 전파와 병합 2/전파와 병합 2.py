import sys
input=sys.stdin.readline

from collections import deque

def to_coor(s):
    i=0
    while s[i].isalpha():i+=1
    y=int(s[i:])-1
    x=0
    for c in s[:i]:
        x*=26
        x+=ord(c)-64
    return y,x-1

R,C=map(int,input().split())

b=[[i.split('+')for i in input().split()]for _ in[0]*R]

edges={}
deg={}

for y in range(R):
    for x in range(C):
        for i in b[y][x]:
            if i=='.':
                continue
            edges[to_coor(i)]=edges.get(to_coor(i),[])
            edges[to_coor(i)]+=(y,x),
            deg[y,x]=deg.get((y,x),0)+1

dq=deque()

for i in edges:
    if deg.get(i,0)<1:dq+=i,

a=0

while dq:
    n=dq.popleft()
    a+=1
    for e in edges.get(n,[]):
        deg[e]-=1
        if deg[e]<1:dq+=e,

print('yneos'[a==len({*edges,*deg})::2])
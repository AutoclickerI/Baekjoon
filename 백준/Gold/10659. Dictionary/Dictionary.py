import sys
input=lambda:sys.stdin.readline().strip()

from collections import deque

def diff(*s):
    for i,j in zip(*s):
        if i!=j:
            return i,j

while n:=int(input()):
    l=[input()for _ in[0]*n]
    f=0
    
    v=set()
    
    for i in range(n):
        for j in range(i+1,n):
            if l[j].startswith(l[i]):
                continue
            if l[i]!=l[j] and l[i].startswith(l[j]):
                f=1
                continue
            v.add(diff(l[i],l[j]))
    
    edges={}
    deg={}
    
    for s,e in v:
        deg[e]=deg.get(e,0)+1
        edges[s]=edges.get(s,[])
        edges[s]+=e,
    
    dq=deque()
    
    for i in range(97,123):
        if deg.get(chr(i),0)<1:dq+=chr(i)
    
    a=[]
    
    while dq:
        n=dq.popleft()
        a+=n,
        for e in edges.get(n,[]):
            deg[e]-=1
            if deg[e]<1:
                dq+=e,
    
    print('yneos'[f or len(a)<26::2])
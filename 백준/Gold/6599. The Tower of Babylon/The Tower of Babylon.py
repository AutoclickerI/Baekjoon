import sys
input=sys.stdin.readline

T=0

def get(n):
    global cnt
    if n in d:
        return d[n]
    ret=d[n]=cnt
    cnt+=1

from collections import deque

while n:=int(input()):
    T+=1
    l=[sorted(map(int,input().split()))for _ in[0]*n]
    cnt=0
    d={}
    ort=[]
    for i,j,k in l:
        ort+=(i,j,k),(i,k,j),(j,k,i)
    
    for i,j,k in ort:
        get((i,j))
    
    edges=[[]for _ in[0]*len(d)]
    c=[0]*len(d)
    v=[0]*len(d)
    deg=[0]*len(d)
    
    for(p1,q1,r1)in ort:
        z=get((p1,q1))
        c[z]=max(r1,c[z])
        for(p2,q2,r2)in ort:
            if p1<p2 and q1<q2:
                edges[get((p2,q2))]+=z,
                deg[z]+=1
    
    dq=deque()
    for i in range(len(d)):
        if deg[i]<1:dq+=i,;v[i]=c[i]
    
    while dq:
        n=dq.popleft()
        for e in edges[n]:
            deg[e]-=1
            v[e]=max(v[e],v[n]+c[e])
            if deg[e]<1:
                dq+=e,
    
    print(f'Case {T}: maximum height =',max(v))
import sys
input=lambda:sys.stdin.readline().strip()

from collections import deque

for T in range(1,int(input())+1):
    R,C=map(int,input().split())
    
    edges={}
    deg={}
    
    aa=set()
    
    for i in zip(*[input()for _ in[0]*R]):
        aa|={*i}
        for j,k in zip(i,i[1:]):
            if j!=k:
                edges[k]=edges.get(k,set())
                edges[k]|={j}
                deg[j]=deg.get(j,set())
                deg[j]|={k}
    
    dq=deque()
    
    for i in*deg,:
        deg[i]=len(deg[i])
    
    for i in aa:
        if i not in deg:
            dq+=i,
    
    a=[]
    
    while dq:
        n=dq.popleft()
        a+=n,
        for e in edges.get(n,[]):
            deg[e]-=1
            if deg[e]<1:
                dq+=e,

    print(f'Case #{T}:',-(len(a)<len(aa))or''.join(a))
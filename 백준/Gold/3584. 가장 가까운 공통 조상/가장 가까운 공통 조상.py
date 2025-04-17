import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

for _ in[0]*int(input()):
    
    N=int(input())
    
    edges=[[]for _ in[0]*-~N]
    deg=[0]*-~N
    
    for _ in[0]*~-N:
        s,e=map(int,input().split())
        edges[s]+=e,
        deg[e]+=1
    
    for i in range(-~N):
        if deg[i]<1:root=i
    
    v=[0]*-~N
    c=[0]*-~N
    d=[0]*-~N
    p=[N.bit_length()*[0]for _ in[0]*-~N]
    
    def DFS(n,depth):
        v[n]=1
        d[n]=depth
        for e in edges[n]:
            if v[e]<1:
                DFS(e,depth+1)
                p[e][0]=n
    
    DFS(root,1)
    
    for j in range(N.bit_length()-1):
        for i in range(N+1):
            p[i][j+1]=p[p[i][j]][j]
    
    def up(n,v):
        if v==0:
            return n
        t=v.bit_length()-1
        return up(p[n][t],v^1<<t)
    
    def lca(a,b):
        if d[b]<d[a]:
            a,b=b,a
        b=up(b,d[b]-d[a])
        
        if a==b:
            return a
        
        for i in range(N.bit_length()-1,-1,-1):
            if p[a][i]!=p[b][i]:
                a=p[a][i]
                b=p[b][i]
        return p[a][0]
    
    s,e=map(int,input().split())
    print(lca(s,e))
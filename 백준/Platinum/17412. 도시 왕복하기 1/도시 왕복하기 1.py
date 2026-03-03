import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

N,P=map(int,input().split())
edges=[[]for _ in[0]*-~N]

for _ in[0]*P:
    s,e=map(int,input().split())
    edges[s]+=[e,1,len(edges[e])],
    edges[e]+=[s,0,len(edges[s])-1],

def max_flow(src,dst):
    flow=0
    while 1:
        level=[-1]*-~N
        level[src]=0
        l=[src]
        for n in l:
            for e,f,_ in edges[n]:
                if level[e]==-1 and f:
                    level[e]=level[n]+1
                    l+=e,
        if level[dst]==-1:
            return flow
        
        def dfs(n,push):
            if n==dst:
                return push
            for i,(e,f,p)in enumerate(edges[n]):
                if f and level[e]==level[n]+1:
                    fl=dfs(e,min(push,f))
                    if fl:
                        edges[n][i][1]-=fl
                        edges[e][p][1]+=fl
                        return fl
            return 0
        
        while fl:=dfs(src,float('inf')):
            flow+=fl

print(max_flow(1,2))
import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**7)

N,P=map(int,input().split())
edges=[[]for _ in[0]*-~N*2]

IN=lambda i:i*2
OUT=lambda i:i*2+1

def add_edge(s,e,f):
    edges[s].append([e,f,len(edges[e])])
    edges[e].append([s,0,len(edges[s])-1])

for i in range(N):
    add_edge(IN(i+1),OUT(i+1),1 if 1<i else float('inf'))

for _ in[0]*P:
    s,e=map(int,input().split())
    add_edge(OUT(s),IN(e),1)
    add_edge(OUT(e),IN(s),1)

def max_flow(src,dst):
    flow=0
    while 1:
        level=[-1]*-~N*2
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

print(max_flow(IN(1),OUT(2)))
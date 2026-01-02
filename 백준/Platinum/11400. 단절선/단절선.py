import sys
sys.setrecursionlimit(9**9)

[V,E],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~V]
for s,e in l:
    edges[s]+=e,
    edges[e]+=s,
low=[-1]*-~V
order=[-1]*-~V
cnt=0
ret=[]

def DFS(n,p):
    global cnt
    cnt+=1
    low[n]=order[n]=cnt
    for e in edges[n]:
        if order[e]<1:
            DFS(e,n)
            low[n]=min(low[n],low[e])
            if order[n]<low[e]:
                ret.append((n,e))
        elif e!=p:
            low[n]=min(low[n],order[e])

DFS(1,-1)
l=sorted(sorted(i)for i in ret)
print(len(l))
for i in l:print(*i)
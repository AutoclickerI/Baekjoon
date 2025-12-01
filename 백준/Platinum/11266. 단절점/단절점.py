import sys
sys.setrecursionlimit(2*10**5)

[V,E],*l=[map(int,i.split())for i in open(0)]
edges=[[]for _ in[0]*-~V]
for s,e in l:edges[s]+=e,;edges[e]+=s,
order=[0]*-~V
low=[0]*-~V
cnt=0
res=[]
def DFS(n,r):
    global cnt
    cut=0
    cld=0
    cnt+=1
    order[n]=low[n]=cnt
    for e in edges[n]:
        if order[e]<1:
            DFS(e,0)
            if not r and order[n]<=low[e]:
                cut=1
            low[n]=min(low[n],low[e])
            cld+=1
        else:
            low[n]=min(low[n],order[e])
    if r and 1<cld:
        cut=1
    if cut:
        res.append(n)

for i in range(1,V+1):
    if order[i]<1:
        DFS(i,1)
print(len(res),*sorted(res))
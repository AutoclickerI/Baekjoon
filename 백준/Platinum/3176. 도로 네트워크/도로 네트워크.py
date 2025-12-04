import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**5)

N=int(input())
edges=[[]for _ in[0]*-~N]
for _ in[0]*~-N:
    s,e,c=map(int,input().split())
    edges[s]+=(e,c),
    edges[e]+=(s,c),

depth=[0]*-~N
parent=[N.bit_length()*[0]for _ in[0]*-~N]
minv=[N.bit_length()*[float('inf')]for _ in[0]*-~N]
maxv=[N.bit_length()*[-float('inf')]for _ in[0]*-~N]

def DFS(n,d):
    depth[n]=d
    for e,c in edges[n]:
        if depth[e]<1:
            parent[e][0]=n
            minv[e][0]=c
            maxv[e][0]=c
            DFS(e,d+1)

DFS(1,1)

for i in range(1,N.bit_length()):
    for n in range(1,N+1):
        parent[n][i]=parent[parent[n][i-1]][i-1]
        minv[n][i]=min(minv[n][i-1],minv[n][i],minv[parent[n][i-1]][i-1])
        maxv[n][i]=max(maxv[n][i-1],maxv[n][i],maxv[parent[n][i-1]][i-1])

def merge(n,p):
    (n1,min1,max1),(n2,min2,max2)=n,p
    return n1,min(min1,min2),max(max1,max2)

def up(n,v):
    if v==0:
        return n,float('inf'),-float('inf')
    else:
        t=v.bit_length()-1
        return merge(up(parent[n][t],v^(1<<t)),(n,minv[n][t],maxv[n][t]))

def lca(a,b):
    if depth[b]<depth[a]:
        a,b=b,a
    b,minv1,maxv1=up(b,depth[b]-depth[a])
    
    if a==b:
        return minv1,maxv1
    
    for i in range(N.bit_length())[::-1]:
        if parent[a][i]!=parent[b][i]:
            minv1=min(minv1,minv[a][i],minv[b][i])
            maxv1=max(maxv1,maxv[a][i],maxv[b][i])
            a=parent[a][i]
            b=parent[b][i]
    
    return min(minv1,minv[a][0],minv[b][0]),max(maxv1,maxv[a][0],maxv[b][0])

for _ in[0]*int(input()):
    print(*lca(*map(int,input().split())))
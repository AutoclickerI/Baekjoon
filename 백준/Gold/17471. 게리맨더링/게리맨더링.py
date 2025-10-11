N=int(input())
*l,=map(int,input().split())
edges=[[*map(int,input().split())][1:]for _ in[0]*N]

def DFS(n,c):
    for e in edges[n]:
        e-=1
        if div[e]==c!=1>v[e]<1:v[e]=1;DFS(e,c)

x=[]

for i in range(1,2**N-1):
    div=f'{i:b}'.zfill(N)
    v=[0]*N
    for c in'01':v[f:=div.find(c)]=1;DFS(f,c)
    x+=[abs(sum(l[i]*(-int(div[i])|1)for i in range(N)))]*all(v)
print(min(x or[-1]))
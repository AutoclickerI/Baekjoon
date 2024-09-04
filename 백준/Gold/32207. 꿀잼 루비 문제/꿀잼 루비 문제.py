N,M,K=map(int,input().split())
B=[[*map(int,input().split())]for _ in[0]*N]
s=set()
price=sorted((-B[i][j],i,j)for i in range(N)for j in range(M))[:21]
V=0

def DFS(n,d,v):
    global V
    V=max(V,v)
    if d==0 or len(price)<=n:
        return
    p,i,j=price[n]
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if (i+dy,j+dx)in s:
            break
    else:
        s.add((i,j))
        DFS(n+1,d-1,v-p)
        s.remove((i,j))
    DFS(n+1,d,v)
DFS(0,K,0)
print(V)
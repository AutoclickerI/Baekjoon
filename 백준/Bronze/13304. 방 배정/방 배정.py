d={}
N,K=map(int,input().split())
for _ in[0]*N:
    p,q=map(int,input().split())
    v=max(5,(q+1)//2*4+p)
    d[v]=d.get(v,0)+1
print(-sum(i//-K for i in d.values()))
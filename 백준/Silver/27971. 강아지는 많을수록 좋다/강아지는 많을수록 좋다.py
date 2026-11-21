N,M,A,B=map(int,input().split())
l=[0]+[-1]*N
for _ in[0]*M:
    p,q=map(int,input().split())
    l[p:q+1]=[-2]*(q-p+1)
for i in range(min(A,B),N+1):
    if l[i]==-2:continue
    p,q=l[i-A],l[i-B]
    if p<0 or q<0:
        if p>=0:
            l[i]=p+1
        if q>=0:
            l[i]=q+1
    else:
        l[i]=min(p,q)+1
print(-1 if l[N]<0 else l[N])
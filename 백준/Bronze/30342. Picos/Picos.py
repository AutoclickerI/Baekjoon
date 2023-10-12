N,M,T,K=map(int,input().split())
ans=0
while N>0:
    ans+=min(N,M)*max(0,K)
    K-=T
    N-=M
print(ans)
N,M,K=map(int,input().split())
l=[input()for _ in[0]*N]
cnt=[[(l[i][j]!='B')^(i+j)%2 for j in range(M)]for i in range(N)]
prefix_sum=[[0]*(M+1)for _ in[0]*(N+1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i+1][j+1]=prefix_sum[i+1][j]+prefix_sum[i][j+1]-prefix_sum[i][j]+cnt[i][j]
m=K*K
for i in range(N-K+1):
    for j in range(M-K+1):
        m=min(m,t:=prefix_sum[i+K][j+K]-prefix_sum[i][j+K]-prefix_sum[i+K][j]+prefix_sum[i][j],K*K-t)
print(m)
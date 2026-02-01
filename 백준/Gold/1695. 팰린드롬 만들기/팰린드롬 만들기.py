N,*l=map(int,open(0).read().split())
dp=[N*[N]for _ in[0]*N]
for s in range(N)[::-1]:
    dp[s][s]=0
    for e in range(s,N):
        if s<N-1:
            if l[s]==l[e]:
                dp[s][e]=min(dp[s][e],dp[s+1][e-1]if s+1<=e-1 else 0)
            dp[s][e]=min(dp[s][e],dp[s+1][e]+1)
        dp[s][e]=min(dp[s][e],dp[s][e-1]+1)
print(dp[0][-1])
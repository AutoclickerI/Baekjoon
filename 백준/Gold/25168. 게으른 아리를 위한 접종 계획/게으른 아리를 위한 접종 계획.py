N,M=map(int,input().split())

dp=[0]*-~N

for s,e,m in sorted([*map(int,input().split())]for _ in[0]*M):
    dp[e]=max(dp[e],dp[s]+m+(6<m))

print(max(dp)+1)
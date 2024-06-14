n, m, x, y=map(int,input().split())
elements = [[*map(int,input().split())]for _ in[0]*n]
dp = [float('inf')] * (m + 1)
dp[0] = 0

for b_i, a_i in elements:
    ndp = [float('inf')] * (m + 1)
    for j in range(m+1):
        if dp[j] != float('inf'):
            for score in range(b_i, a_i + 1):
                if j + score <= m:
                    if score < 10:
                        ndp[j + score] = min(ndp[j + score], dp[j] + x*(0<score))
                    else:
                        ndp[j + score] = min(ndp[j + score], dp[j] + y*(0<score))
    dp=ndp

dp[0] = 0
if dp[m] == float('inf'):
    result = -1
else:
    result = dp[m]
print(result)
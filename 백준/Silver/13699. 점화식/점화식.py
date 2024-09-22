dp=[1]
for i in range(int(input())):dp+=sum(dp[j]*dp[i-j]for j in range(i+1)),
print(dp[-1])
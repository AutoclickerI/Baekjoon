n,*l=map(int,open(0).read().split())
dp=[0]*n
for i in range(1,n):dp[i]=max(dp[j]+(l[j]-l[i])**2for j in range(max(0,i-99),i))
print(max(dp))
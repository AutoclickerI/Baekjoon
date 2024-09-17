s=input()
d=eval('input(),'*int(input()))
dp=[0]*-~len(s)
dp[0]=1
for i in range(len(s)+1):
    for j in range(i):
        if dp[j] and s[j:i]in d:
            dp[i]=1
print(dp[-1])
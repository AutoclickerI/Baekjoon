N,M=map(int,input().split())

# m c
*l,=zip(map(int,input().split()),map(int,input().split()))

dp=[0]*10001

for m,c in l:
    ndp=dp[:c]
    for i in range(10001-c):
        ndp+=max(dp[c+i],dp[i]+m),
    dp=ndp

for i in range(10001):
    if M<=dp[i]:
        print(i)
        break
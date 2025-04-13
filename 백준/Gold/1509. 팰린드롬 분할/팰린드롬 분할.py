S=input()
N=len(S)
*dp,=range(N+1)
p=[N*[0]for _ in[0]*N]

for i in range(N):
    ptr=0
    while 0<=i-ptr and i+ptr<N:
        if S[i-ptr]==S[i+ptr]:
            p[i-ptr][i+ptr]=1
        else:
            break
        ptr+=1
    ptr=0
    while 0<=i-ptr and i+ptr<N-1:
        if S[i-ptr]==S[i+ptr+1]:
            p[i-ptr][i+ptr+1]=1
        else:
            break
        ptr+=1

for i in range(1,N+1):
    for j in range(1,i):
        dp[i]=min(dp[i],dp[j-1]+[i-j+1,1][p[j-1][i-1]],dp[i-1]+1)
print(dp[-1])
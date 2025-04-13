N=int(input())

# dp[i][j][k]: from i to j, ends with k
dp=[[10*[0]for _ in[0]*10]for _ in[0]*10]

for i in range(1,10):
    dp[i][i][i]=1

for _ in[0]*~-N:
    ndp=[[10*[0]for _ in[0]*10]for _ in[0]*10]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for d in-1,1:
                    nk=d+k
                    if nk<0 or 9<nk:
                        continue
                    ndp[min(i,nk)][max(j,nk)][nk]+=dp[i][j][k]
    dp=ndp
print(sum(dp[0][9])%1000000000)
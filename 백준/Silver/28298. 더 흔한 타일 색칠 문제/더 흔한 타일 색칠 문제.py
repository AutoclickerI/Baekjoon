N,M,K=map(int,input().split())
l=[input()for _ in[0]*N]
m=[[{}for _ in[0]*K]for _ in[0]*K]
for i in range(K):
    for j in range(K):
        for li in l[i::K]:
            for k in li[j::K]:
                m[i][j][k]=m[i][j].get(k,0)+1
kcell=[[0 for _ in[0]*K]for _ in[0]*K]
for i in range(K):
    for j in range(K):
        ma=max(m[i][j].values())
        for k in m[i][j]:
            if m[i][j][k]==ma:
                kcell[i][j]=k
ans=[[0]*M for _ in[0]*N]
for i in range(N):
    for j in range(M):
        ans[i][j]=kcell[i%K][j%K]
print(sum(sum(i!=j for i,j in zip(k,l))for k,l in zip(ans,l)))
for i in ans:print(''.join(i))
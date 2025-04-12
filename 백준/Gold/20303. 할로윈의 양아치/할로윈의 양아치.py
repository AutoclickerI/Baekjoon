import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

N,M,K=map(int,input().split())
*c,=map(int,input().split())

edges=[[]for _ in[0]*-~N]

for _ in[0]*M:
    s,e=map(int,input().split())
    edges[e]+=s,
    edges[s]+=e,

v=[0]*-~N
d={}

def DFS(n,t):
    if v[n]:
        return 0,0
    ret=1
    cnt=c[n-1]
    v[n]=t
    for e in edges[n]:
        rv,cv=DFS(e,t)
        ret+=rv
        cnt+=cv
    return ret,cnt

t=1

for i in range(1,N+1):
    if v[i]<1:
        ret,cnt=DFS(i,t)
        if cnt:
            t+=1
            d[ret]=d.get(ret,[])
            d[ret]+=cnt,

dp=[0]*K

for i in d:
    for j in d[i]:
        n_dp=dp[:i]
        for k in range(i,K):
            n_dp+=max(dp[k],dp[k-i]+j),
        dp=n_dp

print(dp[-1])
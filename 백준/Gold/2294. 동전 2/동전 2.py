N,K=map(int,input().split())
v=[0]+[1e99]*K
for _ in[0]*N:
    i=int(input())
    for j in range(i,K+1):
        v[j]=min(v[j],v[j-i]+1)
print(-(1e98<v[-1])or v[-1])
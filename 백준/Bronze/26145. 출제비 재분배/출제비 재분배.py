N,M=map(int,input().split())
l=[*map(int,input().split())]+[0]*M
for i in range(N):
    *t,=map(int,input().split())
    l[i]-=sum(t)
    for i in range(N+M):l[i]+=t[i]
print(*l)
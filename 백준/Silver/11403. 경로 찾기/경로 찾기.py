n=int(input())
l=[[*map(int,input().split())]for _ in[0]*n]
d={}
for i in range(n):
    d[i]=set(j for j in range(n)if l[i][j]==1)
for _ in range(100):
    for i in d:
        t=[*d[i]]
        for j in t:
            d[i]|=d.get(j,{})
l=[[0]*n for _ in[0]*n]
for i in d:
    for j in d[i]:
        l[i][j]=1
[print(*i)for i in l]
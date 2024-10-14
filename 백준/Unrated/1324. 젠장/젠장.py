N,*l=map(int,open(0).read().split())
DP=[0]*N

for i in l[N:]:
    c=0
    for j in range(N):
        if i==l[j]:DP[j]=c+1
        elif i>l[j]:c=max(c,DP[j])

print(max(DP))
N,*l=map(int,open(0).read().split())
assert len(l)==2*N
A=l[:N]
B=l[N:]
DP=[0]*N

for i in range(N):
    cnt=0
    for j in range(N):
        if A[i]==B[j]:
            DP[j]=cnt+1
        elif A[i]>B[j]:
            cnt=max(cnt,DP[j])

print(max(DP))
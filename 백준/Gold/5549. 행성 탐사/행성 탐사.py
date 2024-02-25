import sys
input=sys.stdin.readline
M,N=map(int,input().split())
K=int(input())
b=[[[0]*3]*-~N]
for _ in[0]*M:
    b+=[[0]*3],
    n=0
    for i in input()[:-1]:
        n+=1
        tmp=[p+q-r for p,q,r in zip(b[-2][n],b[-1][-1],b[-2][n-1])]
        tmp['JOI'.find(i)]+=1
        b[-1]+=tmp,
for _ in[0]*K:
    p,q,r,s=map(int,input().split())
    print(*[i+j-k-l for i,j,k,l in zip(b[r][s],b[p-1][q-1],b[r][q-1],b[p-1][s])])
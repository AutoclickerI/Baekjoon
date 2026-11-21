import sys
input=sys.stdin.readline
N,M,Q=map(int,input().split())
row=[0]*N
column=[0]*M
for _ in range(Q):
    a,b,c=map(int,input().split())
    if a-1:
        column[b-1]+=c
    else:
        row[b-1]+=c
[print(*[row[i]+column[j]for j in range(M)])for i in range(N)]
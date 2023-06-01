import sys
input=sys.stdin.readline
N,M=map(int,input().split())
v=[0]*N*2
l=[[]for _ in[0]*N*2]
for _ in[0]*M:
    p,q=map(int,input().split())
    l[p]+=[q]
    l[q]+=[p]
a=0
def DFS(n):
    v[n]=a
    for i in l[n]:
        if v[i]==0:
            DFS(i)
for j in range(N+1):
    if v[j]==0:
        DFS(j)
        a+=1
print(max(v))
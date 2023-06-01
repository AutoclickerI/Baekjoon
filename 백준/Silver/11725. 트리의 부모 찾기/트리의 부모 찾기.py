import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
n=int(input())
d={1:1}
l=[[]for _ in[0]*(n+1)]
for _ in[0]*(n-1):
    p,q=map(int,input().split())
    l[p]+=[q]
    l[q]+=[p]
def DFS(n):
    for i in l[n]:
        if d.get(i):continue
        d[i]=n
        DFS(i)
DFS(1)
for i in range(1,n):print(d[i+1])
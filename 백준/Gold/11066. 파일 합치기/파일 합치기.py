import sys
input=sys.stdin.readline
def recur(s,e):
    if d[s][e]==-1:
        if e-s==1:
            d[s][e]=0
        else:
            d[s][e]=min(recur(s,s+i)+recur(s+i,e)for i in range(1,e-s))+prefix_sum[e]-prefix_sum[s]
    return d[s][e]
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    prefix_sum=[0]+l
    for i in range(n):
        prefix_sum[i+1]+=prefix_sum[i]
    d=[[-1]*(n+1)for _ in[0]*(n+1)]
    print(recur(0,n))
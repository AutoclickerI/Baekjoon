import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[list(map(int,input().split()))for _ in range(N)]
prefix_sum=[[0]*-~N]
for x in range(1,N+1):
    tmp=[0]
    for y in range(1,N+1):
        tmp.append(l[x-1][y-1]+tmp[y-1]+prefix_sum[x-1][y]-prefix_sum[x-1][y-1])
    prefix_sum.append(tmp)
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    print(prefix_sum[x2][y2]-prefix_sum[x2][y1-1]-prefix_sum[x1-1][y2]+prefix_sum[x1-1][y1-1])
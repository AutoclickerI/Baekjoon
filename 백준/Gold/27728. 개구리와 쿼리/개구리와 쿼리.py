import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
minlist=[[2*[10**9]for _ in range(N)]for i in range(N)]
for i in range(N):
    *l,=map(int,input().split())
    for j in range(N):
        minlist[i][-j-1][0]=l[-j-1]+minlist[i][-j][0]*min(j,1)
        minlist[i][-j-1][1]=min(minlist[i][-j-1][0],minlist[i-1][-j-1][1])
for _ in range(Q):
    x,y,L=map(int,input().split())
    print(min(minlist[x-1][y-1][0],min(minlist[x-1][y-1][0]-minlist[x-1][i][0]+min(minlist[x-1-L][i])for i in range(y-1,N))))
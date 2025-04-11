import sys
sys.setrecursionlimit(9**9)

N,M=map(int,input().split())
b=[input()for _ in[0]*N]

check=[M*[0]for _ in[0]*N]

max_cnt=1

def DFS(y,x):
    global max_cnt
    if check[y][x]==max_cnt:
        max_cnt+=1
    if check[y][x]:
        return check[y][x]
    check[y][x]=max_cnt
    dy,dx=((-1,0),(1,0),(0,-1),(0,1))['UDLR'.find(b[y][x])]
    check[y][x]=DFS(y+dy,x+dx)
    return check[y][x]

for y in range(N):
    for x in range(M):
        if check[y][x]<1:
            DFS(y,x)

print(max_cnt-1)
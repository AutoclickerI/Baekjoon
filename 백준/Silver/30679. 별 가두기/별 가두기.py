import sys
sys.setrecursionlimit(9**9)
N,M=map(int,input().split())
K=[[*map(int,input().split())]for _ in[0]*N]
def move(y,x,d):
    if y<0 or N<=y or x<0 or M<=x:
        return 0
    if visited[y][x][d]:
        return 1
    visited[y][x][d]=1
    dy,dx=[(0,1),(1,0),(0,-1),(-1,0)][d]
    return move(y+dy*K[y][x],x+dx*K[y][x],(d+1)%4)
ans=[]
for i in range(N):
    visited=[[4*[0]for _ in[0]*M]for _ in[0]*N]
    if move(i,0,0):
        ans+=i+1,
print(len(ans))
if ans:print(*ans)
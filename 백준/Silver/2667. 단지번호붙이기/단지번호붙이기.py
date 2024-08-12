N=int(input())
board=[input()for _ in range(N)]
visited=[N*[0]for _ in range(N)]

def is_valid(y,x):
    return 0<=y<N and 0<=x<N

def DFS(y,x):
    cnt=0
    if is_valid(y,x):
        if board[y][x]=='0' or visited[y][x]:
            return cnt
        visited[y][x]=1
        cnt+=1
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            cnt+=DFS(y+dy,x+dx) 
    return cnt

ans=[]
for y in range(N):
    for x in range(N):
        v=DFS(y,x)
        if v:
            ans.append(v)

print(len(ans))
for i in sorted(ans):
    print(i)
Y,X=map(int,input().split())
board=[input()for _ in[0]*Y]
cur=[[min(i,j)for i,j in zip(k,k[::-1])]for k in board]
def DFS(i,j):
    for dx,dy in(-1,0),(1,0),(0,1),(0,-1):
        if visited[i+dx][j+dy]==False:
            visited[i+dx][j+dy]=True
            DFS(i+dx,j+dy)
for s in range(~-X//2):
    for e in range(Y):
        if cur[s][e]=='X':
            visited=[[i=='B'for i in l]for l in cur]
            visited[e][s]=True
            visited[e][~s]=True
            DFS(e,s)
            if all(all(i)for i in visited):
                cur[e][s]=cur[e][~s]='W'
                for i in range(X):
                    for j in range(Y):
                        if cur[j][i]=='X':
                            cur[j][i]='Y'
                if all(all(j!='Y'for j in i)for i in cur):
                    continue
                print('YES')
                for i in cur:print(''.join(i))
                exit()
print('NO')
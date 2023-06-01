n=int(input())
l=[[*input()]for _ in[0]*n]
visited=[0]*n*n
num=1
update=0
def DFS(y,x):
    global update
    if visited[y*n+x] or l[y][x]=='0':return
    visited[y*n+x]=num
    for i,j in[[-1,0],[1,0],[0,1],[0,-1]]:
        DFS(max(0,min(y+i,n-1)),max(0,min(x+j,n-1)))
    update=1
for x in range(n):
    for y in range(n):
        DFS(x,y)
        num+=update
        update=0
print(num-1)
print(*sorted([visited.count(i)for i in range(1,num)]),sep='\n')
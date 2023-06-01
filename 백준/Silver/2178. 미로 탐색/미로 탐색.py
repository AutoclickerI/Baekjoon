from collections import*
p,q=map(int,input().split())
l=[input()for _ in[0]*p]
visited=[[0]*q for _ in[0]*p]
def visit(x,y):
    if x<0 or x>=p or y<0 or y>=q:
        return 0
    return int(l[x][y])
Q=deque([(0,0,1)])
visited[0][0]=1
while 0==visited[-1][-1]:
    posx,posy,cnt=Q.popleft()
    for i,j in[[1,0],[-1,0],[0,1],[0,-1]]:
        if visit(posx+i,posy+j)and visited[posx+i][posy+j]==0:
            visited[posx+i][posy+j]=cnt+1
            Q.append((posx+i,posy+j,cnt+1))
print(visited[-1][-1])
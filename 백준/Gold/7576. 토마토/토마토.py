p,q=map(int,input().split())
l=[[*map(int,input().split())]for _ in[0]*q]
from collections import deque
d=[]
for i in range(q):
    for j in range(p):
        if l[i][j]==1:
            d+=[(i,j,0)]
d=deque(d)
def get(x,y):
    if x<0 or y<0 or x>=q or y>=p:
        return -1
    return l[x][y]
while d:
    i,j,n=d.popleft()
    for x,y in[(1,0),(0,1),(-1,0),(0,-1)]:
        if get(i+x,j+y)in[-1,1]:0
        else:l[i+x][j+y]=1;d.append((i+x,j+y,n+1))
f=0
for i in range(q):
    for j in range(p):
        f+=l[i][j]==0
print(-1 if f else n)
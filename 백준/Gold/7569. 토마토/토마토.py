p,q,r=map(int,input().split())
l=[[[*map(int,input().split())]for _ in[0]*q]for _ in[0]*r]
from collections import deque
d=[]
for i in range(r):
    for j in range(q):
        for k in range(p):
            if l[i][j][k]==1:
                d+=[(i,j,k,0)]
d=deque(d)
def get(x,y,z):
    if x<0 or y<0 or z<0 or x>=r or y>=q or z>=p:
        return -1
    return l[x][y][z]
while d:
    i,j,k,n=d.popleft()
    for x,y,z in[(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
        if get(i+x,j+y,k+z)in[-1,1]:0
        else:l[i+x][j+y][k+z]=1;d.append((i+x,j+y,k+z,n+1))
f=0
for i in range(r):
    for j in range(q):
        for k in range(p):
            f+=l[i][j][k]==0
print(-1 if f else n)
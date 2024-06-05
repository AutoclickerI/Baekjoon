import sys
sys.setrecursionlimit(9**9)
h,n,m=map(int,input().split())
b=[input().split()for _ in[0]*n]
v=[m*[1]for _ in[0]*n]
l=[]
def dfs(y,x):
    a=0
    if 0<=y<n and 0<=x<m and b[y][x]=='.'and v[y][x]:
        v[y][x]=0
        a=1
        if y%2:
            for dy,dx in(0,-1),(0,1),(-1,0),(1,0),(-1,1),(1,1):
                a+=dfs(y+dy,x+dx)
        else:
            for dy,dx in(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1):
                a+=dfs(y+dy,x+dx)
    return a
for y in range(n):
    for x in range(m):
        if b[y][x]=='.':
            l+=dfs(y,x),
l.sort()
a=0
while 0<h:
    a+=1
    h-=l.pop()
print(a)
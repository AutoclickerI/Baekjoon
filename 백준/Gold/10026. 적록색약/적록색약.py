import sys
sys.setrecursionlimit(9**9)
n=int(input())
l=[input()for _ in[0]*n]
v=[[0]*n for _ in[0]*n]
def get(x,y):
    if x<0 or y<0 or x>=n or y>=n:return'Z'
    return l[x][y]
a=1
def DFS(x,y,f):
    if get(x,y)in f and v[x][y]==0:
        v[x][y]=a
        DFS(x+1,y,f)
        DFS(x-1,y,f)
        DFS(x,y+1,f)
        DFS(x,y-1,f)
for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            DFS(i,j,l[i][j])
            a+=1
n1=max(max(i)for i in v)
v=[[0]*n for _ in[0]*n]
a=1
for i in range(n):
    for j in range(n):
        if v[i][j]==0:
            DFS(i,j,'B'if l[i][j]=='B' else'RG')
            a+=1
print(n1,max(max(i)for i in v))
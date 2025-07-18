import sys

sys.setrecursionlimit(2*10**5)

(N,M,K),*l,(a1,b1),(a2,b2),(a3,b3),(a4,b4)=[map(int,i.split())for i in open(0)]

b=[N*[0]for _ in[0]*M]
v=[N*[0]for _ in[0]*M]

for x,y in l:
    v[y-1][x-1]=1

def DFS(y,x):
    v[y][x]=c
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<M and 0<=nx<N and v[ny][nx]<1:
            DFS(ny,nx)

c=2
for y in range(M):
    for x in range(N):
        if v[y][x]<1:
            DFS(y,x)
            c+=1

s1={}
for y in range(b1-1,b2):
    for x in range(a1-1,a2):
        if 1<v[y][x]:s1[v[y][x]]=s1.get(v[y][x],0)+1

s2={}
for y in range(b3-1,b4):
    for x in range(a3-1,a4):
        if 1<v[y][x]:s2[v[y][x]]=s2.get(v[y][x],0)+1

a=0
for i in{*s1}&{*s2}:
    a+=s1[i]*s2[i]
print(a)
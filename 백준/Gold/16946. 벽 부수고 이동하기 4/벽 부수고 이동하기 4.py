import sys
sys.setrecursionlimit(9**8)

N,M=map(int,input().split())
b=[input()for _ in[0]*N]

v=[M*[0]for _ in[0]*N]

d={}

def DFS(y,x,t):
    if v[y][x] or b[y][x]!='0':
        return 0
    v[y][x]=t
    ret=1
    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
        if 0<=y+dy<N and 0<=x+dx<M:
            ret+=DFS(y+dy,x+dx,t)
    return ret

t=1

for y in range(N):
    for x in range(M):
        c=DFS(y,x,t)
        if c:
            d[t]=c
            t+=1
        
for y in range(N):
    for x in range(M):
        s=set()
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            if 0<=y+dy<N and 0<=x+dx<M and b[y+dy][x+dx]=='0':
                s|={v[y+dy][x+dx]}
        print(end=['0',str((1+sum(d[i]for i in s))%10)][v[y][x]<1])
    print()
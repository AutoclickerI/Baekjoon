import sys
sys.setrecursionlimit(2*10**5)

N,M=map(int,input().split())
b=[input()for _ in[0]*N]
v=[M*[-1]for _ in[0]*N]

def check(y,x):
    if 0<=y<N and 0<=x<M:
        if-1<v[y][x]:
            return v[y][x]
        v[y][x]=0
        dy,dx=[(-1,0),(0,1),(1,0),(0,-1)]['URD'.find(b[y][x])]
        v[y][x]=check(y+dy,x+dx)
        return v[y][x]
    return 1

print(sum(check(y,x)for y in range(N)for x in range(M)))
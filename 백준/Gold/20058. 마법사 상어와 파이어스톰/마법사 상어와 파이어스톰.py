import sys
sys.setrecursionlimit(2*10**5)

def split(arr,n):
    r=2**n
    return[[[[*k][j:j+r]for k in i]for j in range(0,2**N,r)]for i in zip(*[iter(arr)]*r)]

def merge(arr):
    ret=[]
    for i in arr:
        tmp=[[]for _ in[0]*len(i[0])]
        for j in i:
            for k in range(len(j)):
                tmp[k]+=j[k]
        ret+=tmp
    return ret

N,Q=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*2**N]

for i in map(int,input().split()):
    b=split(b,i)
    for y in range(len(b)):
        for x in range(len(b)):
            b[y][x]=[[*i][::-1]for i in zip(*b[y][x])]
    b=merge(b)
    v=[2**N*[0]for _ in[0]*2**N]
    for y in range(len(b)):
        for x in range(len(b)):
            c=0
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                ny,nx=y+dy,x+dx
                c+=0<=ny<2**N and 0<=nx<2**N and 0<b[ny][nx]
            v[y][x]=c<3
    for y in range(len(b)):
        for x in range(len(b)):
            if b[y][x]:b[y][x]-=v[y][x]

print(sum(sum(b,[])))
m=0
v=[2**N*[0]for _ in[0]*2**N]
def DFS(y,x):
    f=0
    if 0<=y<2**N and 0<=x<2**N and b[y][x]and v[y][x]<1:
        v[y][x]=1
        f=1
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            f+=DFS(y+dy,x+dx)
    return f

for y in range(len(b)):
    for x in range(len(b)):
        m=max(m,DFS(y,x))
print(m)
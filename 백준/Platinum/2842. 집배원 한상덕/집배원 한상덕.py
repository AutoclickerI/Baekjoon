N=int(input())
b=[input()for _ in[0]*N]
h=[[*map(int,input().split())]for _ in[0]*N]

pl=sorted({*sum(h,[])})

K=[]

for y in range(N):
    for x in range(N):
        if b[y][x]=='K':
            K+=(y,x),
        if b[y][x]=='P':
            P=y,x

m=float('inf')

def check():
    v=[N*[0]for _ in[0]*N]
    minh=pl[s]
    maxh=pl[e]+1
    y,x=P
    if minh<=h[y][x]<maxh:
        v[y][x]=1
        l=[(y,x)]
        for y,x in l:
            for dy in-1,0,1:
                for dx in-1,0,1:
                    if dy==dx==0:continue
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<N and v[ny][nx]<1 and minh<=h[ny][nx]<maxh:
                        v[ny][nx]=1
                        l+=(ny,nx),
        for y,x in K:
            if v[y][x]<1:
                return 0
        return 1
    return 0

s=e=0

while e<len(pl):
    while s<=e and check():
        m=min(m,pl[e]-pl[s])
        s+=1
    e+=1
print(m)
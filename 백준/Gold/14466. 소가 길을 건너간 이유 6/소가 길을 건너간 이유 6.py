[N,K,R],*l=[[*map(int,i.split())]for i in open(0)]

v=[N*[0]for _ in[0]*N]

rd=set()

def norm(a,b,c,d):
    p,q=sorted([(a,b),(c,d)])
    return*p,*q

for a,b,c,d in l[:R]:
    rd.add(norm(a-1,b-1,c-1,d-1))

cnt=0

def BFS(y,x):
    global cnt
    cnt+=1
    v[y][x]=cnt
    l=[(y,x)]
    for y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N and norm(y,x,ny,nx)not in rd and v[ny][nx]<1:
                v[ny][nx]=cnt
                l+=(ny,nx),

for y in range(N):
    for x in range(N):
        if v[y][x]<1:
            BFS(y,x)

kl=[v[y-1][x-1]for y,x in l[R:]]
print(sum(i!=j for i in kl for j in kl)//2)
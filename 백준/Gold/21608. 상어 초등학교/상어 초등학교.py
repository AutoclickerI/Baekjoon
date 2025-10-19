[N],*l=[map(int,i.split())for i in open(0)]
b=[N*[0]for _ in[0]*N]

def f(i):
    y,x=i//N,i%N
    friends=0
    empty=0
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<N and 0<=nx<N:
            friends+=b[ny][nx] in fr
            empty+=b[ny][nx]<1
    return -(b[y][x]<1),-friends,-empty,y,x

d={}

for n,*fr in l:
    i=min(range(N*N),key=f)
    b[i//N][i%N]=n
    d[n]=fr
sc=0
for y in range(N):
    for x in range(N):
        c=0
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N:
                c+=b[ny][nx] in d[b[y][x]]
        sc+=c and 10**(c-1)
print(sc)
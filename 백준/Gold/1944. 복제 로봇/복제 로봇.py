N,M=map(int,input().split())
B=[input()for _ in[0]*N]

P=[]
S=0

for y in range(N):
    for x in range(N):
        if B[y][x]=='S':
            S=(y,x)
        elif B[y][x]=='K':
            P+=(y,x),

P=[S]+P
I=[N*[-1]for _ in[0]*N]

for i,(y,x)in enumerate(P):
    I[y][x]=i

E=[]

def bfs(s):
    d=[N*[-1]for _ in[0]*N]
    y,x=P[s]
    d[y][x]=0
    l=[(y,x)]
    for y,x in l:
        if s<I[y][x]:
            E.append((d[y][x],s,I[y][x]))
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if B[ny][nx]!='1'and d[ny][nx]<0:
                d[ny][nx]=d[y][x]+1
                l+=(ny,nx),

for i in range(M+1):
    bfs(i)

*p,=range(M+1)

def find(n):
    if n!=p[n]:
        p[n]=find(p[n])
    return p[n]

c=r=0
for w,s,e in sorted(E):
    s=find(s)
    e=find(e)
    if s-e:
        p[e]=s
        r+=w
        c+=1

print(-(c!=M)or r)
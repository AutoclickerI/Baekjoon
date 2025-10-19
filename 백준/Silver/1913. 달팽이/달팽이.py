N,n=map(int,open(0))
l=[N*[0]for _ in[0]*N]
y=x=N//2
l[y][x]=1
f=0
d=0
c=1
z=0
for i in range(N*N):
    l[y][x]=i+1
    dy,dx=[(-1,0),(0,1),(1,0),(0,-1)][d%4]
    y+=dy
    x+=dx
    z+=1
    if z==c:
        d+=1
        c+=f
        f^=1
        z=0
for i in l:
    print(*i)
for y in range(N):
    for x in range(N):
        if l[y][x]==n:
            exit(print(y+1,x+1))
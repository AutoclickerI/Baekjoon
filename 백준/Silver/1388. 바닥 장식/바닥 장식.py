N,M=map(int,input().split())
b=[input()for _ in[0]*N]
v=[M*[0]for _ in[0]*N]
def travel(y,x,dy,dx,c):
    if 0<=y<N and 0<=x<M and b[y][x]==c:
        v[y][x]=1
        travel(y+dy,x+dx,dy,dx,c)
c=0
for y in range(N):
    for x in range(M):
        if v[y][x]<1:
            if b[y][x]=='|':
                travel(y,x,1,0,'|')
            else:
                travel(y,x,0,1,'-')
            c+=1
print(c)
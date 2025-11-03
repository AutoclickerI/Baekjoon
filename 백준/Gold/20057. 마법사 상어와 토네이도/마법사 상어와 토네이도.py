[N],*b=[[*map(int,i.split())]for i in open(0)]
sa=sum(sum(i)for i in b)
l=[]
i=1
while len(l)<N*N:
    l+=[1]*i+[2]*i
    l+=[3]*-~i+[4]*-~i
    i+=2
l=l[:N*N]
y=x=N//2
move=[[0,0,2,0,0],
      [0,10,7,1,0],
      [5,0,0,0,0],
      [0,10,7,1,0],
      [0,0,2,0,0]]
*moveu,=zip(*move)
db={1:move,4:moveu,2:moveu[::-1],3:[i[::-1]for i in move]}
for i in l:
    dy,dx=[(0,-1),(1,0),(0,1),(-1,0)][i-1]
    ny,nx=y+dy,x+dx
    mb=db[i]
    deltas=[5*[0]for _ in[0]*5]
    for yy in range(5):
        for xx in range(5):
            deltas[yy][xx]=mb[yy][xx]*b[ny][nx]//100
    deltas[2+dy][2+dx]+=b[ny][nx]-sum(sum(i)for i in deltas)
    b[ny][nx]=0
    for yy in range(5):
        for xx in range(5):
            nny,nnx=ny+yy-2,nx+xx-2
            if 0<=nny<N and 0<=nnx<N:
                b[nny][nnx]+=deltas[yy][xx]
    y,x=ny,nx
print(sa-sum(sum(i)for i in b))
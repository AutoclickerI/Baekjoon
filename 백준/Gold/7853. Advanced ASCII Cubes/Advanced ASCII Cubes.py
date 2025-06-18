N,M=map(int,input().split())
A=[[*map(int,input().split())]for _ in[0]*N]

W=N*2+M*4+1
H=0
v=N*2+1
for i in A:
    H=max(H,v+max(i)*3)
    v-=2
b=[W*['.']for _ in[0]*H]

def draw(y,x):
    b[y][x]=b[y][x+4]=b[y-2][x+6]=b[y-3][x]=b[y-3][x+4]=b[y-5][x+2]=b[y-5][x+6]='+'
    b[y][x+1]=b[y][x+2]=b[y][x+3]=b[y-3][x+1]=b[y-3][x+2]=b[y-3][x+3]=b[y-5][x+3]=b[y-5][x+4]=b[y-5][x+5]='-'
    b[y-1][x+5]=b[y-4][x+1]=b[y-4][x+5]='/'
    b[y-1][x]=b[y-1][x+4]=b[y-2][x]=b[y-2][x+4]=b[y-3][x+6]=b[y-4][x+6]='|'
    b[y-1][x+1]=b[y-1][x+2]=b[y-1][x+3]=b[y-2][x+1]=b[y-2][x+2]=b[y-2][x+3]=b[y-2][x+5]=b[y-3][x+5]=b[y-4][x+2]=b[y-4][x+3]=b[y-4][x+4]=' '

for i in range(N):
    for j in range(M):
        y,x=H-(N-1-i)*2-1,4*j+(N-1-i)*2
        draw(y,x)
        for _ in range(A[i][j]-1):
            y-=3
            draw(y,x)

for i in b:
    print(*i,sep='')
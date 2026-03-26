N,*b=open(0)
N=int(N)

A=[N*[0]for _ in[0]*N] # (1,2)->x
B=[N*[0]for _ in[0]*N] # (2,1)->x
C=[N*[0]for _ in[0]*N] # x->(N-1,N)
D=[N*[0]for _ in[0]*N] # x->(N,N-1)

A[0][1]=B[1][0]=C[N-2][N-1]=D[N-1][N-2]=1
for y in range(N):
    for x in range(1,N):
        if b[y][x]=='.':
            A[y][x]^=A[y][x-1]^A[y-1][x]

for y in range(1,N):
    for x in range(N):
        if b[y][x]=='.':
            B[y][x]^=B[y][x-1]^B[y-1][x]

for y in range(N-1)[::-1]:
    for x in range(N)[::-1]:
        if b[y][x]=='.':
            C[y][x]^=C[y][(x+1)%N]^C[(y+1)%N][x]

for y in range(N)[::-1]:
    for x in range(N-1)[::-1]:
        if b[y][x]=='.':
            D[y][x]^=D[y][(x+1)%N]^D[(y+1)%N][x]

r=[['#W'[j=='.']for j in i[:-1]]for i in b]

for s in range(1,2*N-2):
    S_BD=S_BC=S_AD=S_AC=0

    y0=max(0,s-N+1)
    y1=min(N-1,s)

    for y in range(y0,y1+1):
        x=s-y
        if b[y][x]=='#':
            continue
        S_BD^=B[y][x]&D[y][x]
        S_BC^=B[y][x]&C[y][x]
        S_AD^=A[y][x]&D[y][x]
        S_AC^=A[y][x]&C[y][x]

    for y in range(y0,y1+1):
        x=s-y
        if b[y][x]=='#':
            continue
        f=0
        f^=A[y][x]&C[y][x]&S_BD
        f^=A[y][x]&D[y][x]&S_BC
        f^=B[y][x]&C[y][x]&S_AD
        f^=B[y][x]&D[y][x]&S_AC
        if f:
            r[y][x]='B'

for i in r:
    print(*i,sep='')
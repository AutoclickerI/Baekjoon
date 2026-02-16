N,M,P=map(int,input().split())
*S,=map(int,input().split())
b=[[*input()]for _ in[0]*N]

init=[[]for _ in[0]*9]

for y in range(N):
    for x in range(M):
        if b[y][x]not in'.#':
            init[int(b[y][x])-1]+=(0,y,x),

f=1
while f:
    f=0
    for i in range(P):
        if init[i]:
            for _ in range(S[i]):
                if not init[i]:
                    break
                t=[]
                for c,y,x in init[i]:
                    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<N and 0<=nx<M and b[ny][nx]=='.':
                            t+=(c+1,ny,nx),
                            b[ny][nx]=int(i+1)
                            f=1
                init[i]=t

d=[0]*P
for y in range(N):
    for x in range(M):
        c=b[y][x]
        if c not in[*'.#']:d[int(c)-1]+=1
print(*d)
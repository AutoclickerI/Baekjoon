K,R,N=input().split()
b=[8*[0]for _ in[0]*8]
y,x=R
sy,sx=(48-ord(x))%8,ord(y)-65
b[sy][sx]=1
y,x=K
y,x=(48-ord(x))%8,ord(y)-65
b[y][x]=2
for _ in[0]*int(N):
    dy,dx=[(0,1),(0,-1),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)][(*'RLBT','RT','LT','RB','LB').index(input())]
    ny,nx=y+dy,x+dx
    if 0<=ny<8 and 0<=nx<8:
        if b[ny][nx]<1:
            b[ny][nx]=2
            b[y][x]=0
            y,x=ny,nx
        elif 0<=ny+dy<8 and 0<=nx+dx<8:
            b[ny+dy][nx+dx]=1
            b[ny][nx]=2
            b[y][x]=0
            y,x=ny,nx
            sy,sx=ny+dy,nx+dx
print(chr(65+x)+str(8-y))
print(chr(65+sx)+str(8-sy))
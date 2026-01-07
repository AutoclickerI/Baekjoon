[M,S],*l,[sy,sx]=[map(int,i.split())for i in open(0)]

sy-=1
sx-=1

fish=[[8*[0]for _ in[0]*4]for _ in[0]*4]
last_smell=[4*[-float('inf')]for _ in[0]*4]
for y,x,d in l:
    fish[y-1][x-1][d-1]+=1

for t in range(S):
    nf=[[8*[0]for _ in[0]*4]for _ in[0]*4]
    for y in range(4):
        for x in range(4):
            for d in range(8):
                if fish[y][x][d]:
                    for dd in range(8,0,-1):
                        nd=d+dd&7
                        dy,dx=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)][nd]
                        ny,nx=y+dy,x+dx
                        if 0<=ny<4 and 0<=nx<4 and (ny,nx)!=(sy,sx) and last_smell[ny][nx]+2<t:
                            nf[ny][nx][nd]+=fish[y][x][d]
                            break
                    else:
                        nf[y][x][d]+=fish[y][x][d]

    del_fish=-float('inf')
    for mv in range(4**3):
        nft=[[j[:]for j in i]for i in nf]
        mv=[mv//16,mv//4%4,mv%4]
        y,x=sy,sx
        f=1
        c=0
        for d in mv:
            dy,dx=[(-1,0),(0,-1),(1,0),(0,1)][d]
            y,x=y+dy,x+dx
            if 0<=y<4 and 0<=x<4:
                c+=sum(nft[y][x])
                nft[y][x]=[0]
            else:
                f=0
        if f:
            if del_fish<c:
                del_fish=c
                del_mv=mv
    
    for d in del_mv:
        dy,dx=[(-1,0),(0,-1),(1,0),(0,1)][d]
        sy,sx=sy+dy,sx+dx
        if sum(nf[sy][sx]):
            last_smell[sy][sx]=t
        nf[sy][sx]=[0]*8
    for y in range(4):
        for x in range(4):
            for d in range(8):
                nf[y][x][d]+=fish[y][x][d]
    fish=nf

print(sum(sum(sum(j)for j in i)for i in fish))
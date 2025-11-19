N,M,k=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
*d,=map(int,input().split())
t=[[[*map(int,input().split())]for _ in[0]*4]for _ in[0]*M]

v=[N*[-10**18]for _ in[0]*N]
cnt=0
num_shark=M
while 1<num_shark and cnt<1001:
    for y in range(N):
        for x in range(N):
            if b[y][x]:
                v[y][x]=cnt*M+b[y][x]-1
    tmp=[N*[0]for _ in[0]*N]
    for y in range(N):
        for x in range(N):
            if b[y][x]:
                for dd in t[b[y][x]-1][d[b[y][x]-1]-1]:
                    dy,dx=[(-1,0),(1,0),(0,-1),(0,1)][dd-1]
                    ny,nx=y+dy,x+dx
                    if 0<=ny<N and 0<=nx<N and v[ny][nx]//M+k<=cnt:
                        if tmp[ny][nx]<1:
                            tmp[ny][nx]=b[y][x]
                            num_shark+=1
                        elif b[y][x]<tmp[ny][nx]:
                            tmp[ny][nx]=b[y][x]
                        num_shark-=1
                        d[b[y][x]-1]=dd
                        break
                else:
                    for dd in t[b[y][x]-1][d[b[y][x]-1]-1]:
                        dy,dx=[(-1,0),(1,0),(0,-1),(0,1)][dd-1]
                        ny,nx=y+dy,x+dx
                        if 0<=ny<N and 0<=nx<N and v[ny][nx]%M+1==b[y][x]:
                            if tmp[ny][nx]<1:
                                tmp[ny][nx]=b[y][x]
                                num_shark+=1
                            elif b[y][x]<tmp[ny][nx]:
                                tmp[ny][nx]=b[y][x]
                            num_shark-=1
                            d[b[y][x]-1]=dd
                            break
    b=tmp
    cnt+=1
print(-(cnt==1001)or cnt)
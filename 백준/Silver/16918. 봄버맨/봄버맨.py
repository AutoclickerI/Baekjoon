R,C,N=map(int,input().split())
b=[input()for _ in[0]*R]
v=[C*[0]for _ in[0]*R]
for y in range(R):
    for x in range(C):
        if b[y][x]=='O':v[y][x]=1
cnt=1
for i in range(N-1):
    if i%2:
        for y in range(R):
            for x in range(C):
                if v[y][x]==cnt:
                    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<R and 0<=nx<C and v[ny][nx]!=cnt:
                            v[ny][nx]=0
        for y in range(R):
            for x in range(C):
                if v[y][x]==cnt:
                    v[y][x]=0
        cnt+=1
    else:
        for y in range(R):
            for x in range(C):
                if v[y][x]==0:
                    v[y][x]=cnt+1
for i in v:
    print(*['.O'[0<j]for j in i],sep='')
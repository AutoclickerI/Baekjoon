b=[[*input()]for _ in[0]*12]

def DFS(y,x,c,m):
    f=1
    v[y][x]=1
    if m:
        b[y][x]='.'
    for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
        ny,nx=y+dy,x+dx
        if 0<=ny<12 and 0<=nx<6 and v[ny][nx]<1 and b[ny][nx]==c:
            f+=DFS(ny,nx,c,m)
    return f

cnt=0
while 1:
    v=[6*[0]for _ in[0]*12]
    pos=[]
    for y in range(12):
        for x in range(6):
            if v[y][x]<1 and b[y][x]!='.':
                if 3<DFS(y,x,b[y][x],0):
                    pos+=(y,x),
    if not pos:
        break
    cnt+=1
    v=[6*[0]for _ in[0]*12]
    for y,x in pos:
        DFS(y,x,b[y][x],1)
    b=[[*i]for i in zip(*[('.'*12+''.join(i).replace('.',''))[-12:]for i in zip(*b)])]
print(cnt)
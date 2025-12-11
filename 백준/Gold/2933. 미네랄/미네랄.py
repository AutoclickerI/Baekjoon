R,C=map(int,input().split())
b=[[*input()]for _ in[0]*R]
input()
s=0
for i in map(int,input().split()):
    s^=1
    y=R-i
    if s:
        for x in range(C):
            if b[y][x]=='x':
                break
        else:
            continue
    else:
        for x in range(C)[::-1]:
            if b[y][x]=='x':
                break
        else:
            continue
    b[y][x]='.'
    v=[C*[0]for _ in[0]*R]
    cnt=0
    d={}
    for y in range(R):
        for x in range(C):
            if b[y][x]=='x' and v[y][x]<1:
                cnt+=1
                d[cnt]=l=[(y,x)]
                v[y][x]=1
                for y,x in l:
                    for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<R and 0<=nx<C and v[ny][nx]<1 and b[ny][nx]=='x':
                            v[ny][nx]+=1
                            l+=(ny,nx),
    down=[]
    for i in d:
        if max(d[i])[0]!=R-1:
            down=d[i]
    if down:
        md=max(down)[0]
        for y,x in down:
            b[y][x]='.'
        while md+1<R and all(b[y+1][x]=='.'for y,x in down):
            down=[(y+1,x)for y,x in down]
            md+=1
        for y,x in down:
            b[y][x]='x'
for i in b:print(*i,sep='')
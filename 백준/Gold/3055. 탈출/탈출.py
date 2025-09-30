R,C=map(int,input().split())
b=[input()for _ in[0]*R]

def step():
    global b
    tmp=[[*i]for i in b]
    for y in range(R):
        for x in range(C):
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                ny,nx=y+dy,x+dx
                if 0<=ny<R and 0<=nx<C and tmp[y][x]=='.'and b[ny][nx]=='*':
                    tmp[y][x]='*'
    b=tmp

for y in range(R):
    for x in range(C):
        if b[y][x]=='S':
            l={(y,x)}
cnt=0
while l:
    step()
    tmp=set()
    cnt+=1
    for y,x in l:
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C:
                if b[ny][nx]=='.':
                    tmp|={(ny,nx)}
                if b[ny][nx]=='D':
                    exit(print(cnt))
    l=tmp
print('KAKTUS')
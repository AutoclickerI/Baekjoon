n=int(input())
b=[input()for _ in[0]*n]
o=[[*input()]for _ in[0]*n]
f=0
for y in range(n):
    for x in range(n):
        if o[y][x]=='x':
            f|=b[y][x]=='*'
            c=0
            for dy in-1,0,1:
                for dx in-1,0,1:
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n:
                        c+=b[ny][nx]=='*'
            o[y][x]=c
if f:
    for y in range(n):
        for x in range(n):
            if b[y][x]=='*':
                o[y][x]='*'
for i in o:
    print(*i,sep='')
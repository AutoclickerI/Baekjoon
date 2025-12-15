R,C=map(int,input().split())
b=[input()for _ in[0]*R]
v=[[*i]for i in b]

for y in range(R):
    for x in range(C):
        c=4
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<R and 0<=nx<C and b[ny][nx]=='X':
                c-=1
        if 2<c:v[y][x]='.'
while v and{*v[-1]}=={'.'}:v.pop()
while v and{*v[0]}=={'.'}:v.pop(0)
*v,=zip(*v)
while v and{*v[-1]}=={'.'}:v.pop()
while v and{*v[0]}=={'.'}:v.pop(0)
*v,=zip(*v)
for i in v:print(*i,sep='')
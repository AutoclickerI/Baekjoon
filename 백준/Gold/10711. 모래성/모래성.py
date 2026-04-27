H,W=map(int,input().split())
b=[input()for _ in[0]*H]

c=[W*[0]for _ in[0]*H]
v=[W*[0]for _ in[0]*H]
l=[]

for y in range(H):
    for x in range(W):
        if b[y][x]!='.':
            for dy in-1,0,1:
                for dx in-1,0,1:
                    ny,nx=y+dy,x+dx
                    if b[ny][nx]=='.':
                        c[y][x]+=1
            if int(b[y][x])<=c[y][x]:
                v[y][x]=1
                l+=(y,x,1),

r=0
for y,x,t in l:
    r=max(r,t)
    for dy in-1,0,1:
        for dx in-1,0,1:
            ny,nx=y+dy,x+dx
            if b[ny][nx]!='.'and v[ny][nx]<1:
                c[ny][nx]+=1
                if int(b[ny][nx])<=c[ny][nx]:
                    v[ny][nx]=1
                    l+=(ny,nx,t+1),

print(r)
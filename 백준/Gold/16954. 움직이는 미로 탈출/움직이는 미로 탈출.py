*b,=open(0)
v={(7,0)}
while v:
    tmp=set()
    for y,x in v:
        if b[y][x]=='#':
            continue
        for dy in-1,0,1:
            for dx in-1,0,1:
                ny,nx=y+dy,x+dx
                if 0<=ny<8 and 0<=nx<8 and b[ny][nx]=='.':
                    tmp.add((ny,nx))
    if(0,7)in tmp:
        print(1)
        break
    v=tmp
    b=['.'*8]+b
else:
    print(0)
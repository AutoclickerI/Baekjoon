[R,C],*b=[[*map(int,i.split())]for i in open(0)]

if R%2:
    print(R//2*('R'*~-C+'D'+'L'*~-C+'D')+'R'*~-C)
elif C%2:
    print(C//2*('D'*~-R+'R'+'U'*~-R+'R')+'D'*~-R)
else:
    ty,tx=min([(y,x)for y in range(R)for x in range(C)if y+x&1],key=lambda s:b[s[0]][s[1]])
    c=R//2-1
    while 1<ty:
        print(end='R'*~-C+'D'+'L'*~-C+'D')
        ty-=2
        c-=1
    y=x=0
    d=0
    while(y,x)!=(1,C-1):
        dy,dx=[(1,0),(0,1),(-1,0),(0,1)][d%4]
        ny,nx=y+dy,x+dx
        if(ny,nx)==(ty,tx):
            d+=3
            continue
        print(end='DRUR'[d%4])
        d+=1
        y,x=ny,nx
    for _ in c*[0]:
        print('D'+'L'*~-C+'D'+'R'*~-C,end='')
for T in[0]*int(input()):
    n=int(input())
    b=[input()for _ in[0]*n]
    p=[]
    for y in range(n):
        for x in range(n):
            if b[y][x]=='s':
                sy,sx=y,x
            if b[y][x]=='p':
                p+=(y,x),
    my,mx=min(p,key=lambda s:((s[0]-sy)**2+(s[1]-sx)**2,x,y))
    print(f'({sy},{sx}):({my},{mx}):{((my-sy)**2+(mx-sx)**2)**.5:.2f}')
for i in[*open(0)][1:]:
    mx=my=Mx=My=y=x=d=0
    for c in i[:-1]:
        dy,dx=[(1,0),(0,-1),(-1,0),(0,1)][d]
        if c=='F':
            y+=dy;x+=dx
        if c=='B':
            y-=dy;x-=dx
        if c=='L':
            d=d+1&3
        if c=='R':
            d=d+3&3
        mx=min(mx,x)
        my=min(my,y)
        Mx=max(Mx,x)
        My=max(My,y)
    print((My-my)*(Mx-mx))
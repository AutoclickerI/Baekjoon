for _ in[0]*int(input()):
    x=y=p=0
    for i in input():
        if i=='?':
            p+=1
        if i=='U':
            y+=1
        if i=='D':
            y-=1
        if i=='L':
            x-=1
        if i=='R':
            x+=1
    print(x-p,y-p,x+p,y+p)
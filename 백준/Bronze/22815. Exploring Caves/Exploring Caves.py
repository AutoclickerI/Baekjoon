for _ in[0]*int(input()):
    x=y=0
    m=(0,0,0)
    while 1:
        a,b=map(int,input().split())
        if a==b==0:break
        x+=a
        y+=b
        m=max(m,(x*x+y*y,x,y))
    print(*m[1:])
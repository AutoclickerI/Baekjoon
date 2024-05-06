while'1'<(s:=input()):
    n,w,l,h,a,m=map(int,s.split())
    v=w*l+2*(w+l)*h
    for _ in[0]*m:v-=eval(input().replace(*' *'))
    print(0-(v*n)//-a)
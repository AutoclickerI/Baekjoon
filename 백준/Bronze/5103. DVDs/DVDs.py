while'#'<(s:=input()):
    m,n=map(int,input().split())
    for i in range(int(input())):o=input();n=max(0,min(m,n-int(o[1:])*(2*('S'<o)-1)))
    print(s,n)
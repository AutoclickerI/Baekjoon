while n:=int(input()):
    s=set()
    f=1
    for _ in[0]*n:
        a,b,c,d=map(int,input().replace(*'-:').split(':'))
        t={*range(a*60+b,c*60+d)}
        if s&t:f=0
        s|=t
    print(f*'no '+'conflict')
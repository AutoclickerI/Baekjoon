while'0#'<(s:=input()):
    p,_,q=map(int,s.split())
    d={str(i+1):0 for i in range(q)}
    for _ in[0]*p:
        for i in input().split():d[i]+=1
    m=min(d.values())
    print(*[i+1 for i in range(q)if d[str(1+i)]==m])
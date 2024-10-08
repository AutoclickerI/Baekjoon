while'#'<(s:=input()):
    S,*l=s.split()
    S=int(S)
    h=[0]*21
    h[S]=1    
    for i in l:
        S+=int(i[1:])*((i[0]>'D')*2-1)
        if 20>=S>=1>h[S]:h[S]=1
        else:s=0
    if s:print(*[i for i in range(1,21)if h[i]<1]or['none'])
    else:print('illegal')
while'1'<(s:= input()):
    B,N=map(int,s.split())
    R=[0,*map(int,input().split())]
    for _ in[0]*N:D,C,V=map(int,input().split());R[D]-=V;R[C]+=V
    print('SN'[any(i<0for i in R)])
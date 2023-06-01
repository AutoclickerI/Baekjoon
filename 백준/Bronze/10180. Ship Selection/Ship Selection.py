for _ in[0]*int(input()):
    N,D=map(int,input().split())
    l=[]
    for _ in[0]*N:
        p,q,r=map(int,input().split())
        l+=[p*q/r>=D]
    print(sum(l))
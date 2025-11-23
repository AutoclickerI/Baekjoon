from itertools import*
for _ in[0]*int(input()):
    N=int(input())
    [Y,X],*l=[[*map(int,input().split())]for _ in[0]*N]
    for y,x in l:
        Y-=y
        X-=x
    m=float('inf')
    for i in combinations(l,N//2-1):
        ny,nx=Y,X
        for y,x in i:
            ny+=2*y
            nx+=2*x
        m=min(m,ny**2+nx**2)
    print(m**.5)
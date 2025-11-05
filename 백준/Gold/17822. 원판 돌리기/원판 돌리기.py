N,M,T=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]
for _ in[0]*T:
    x,d,k=map(int,input().split())
    for i in range(x-1,N,x):
        if d==0:
            b[i]=(b[i]*2)[-k%M:-k%M+M]
        else:
            b[i]=(b[i]*2)[k%M:k%M+M]
    nb=[i[:]for i in b]
    f=1
    for y in range(N):
        for x in range(M):
            if b[y][x]==b[y][(x+1)%M]!=0:
                nb[y][x]=nb[y][(x+1)%M]=0
                f=0
            if y<N-1 and b[y][x]==b[y+1][x]!=0:
                nb[y][x]=nb[y+1][x]=0
                f=0
    b=nb
    if f:
        l=[v for i in b for v in i if v]
        numl=len(l)
        avg=sum(l)
        for y in range(N):
            for x in range(M):
                if b[y][x]:
                    if avg<b[y][x]*numl:
                        b[y][x]-=1
                    elif b[y][x]*numl<avg:
                        b[y][x]+=1
print(sum(sum(i)for i in b))
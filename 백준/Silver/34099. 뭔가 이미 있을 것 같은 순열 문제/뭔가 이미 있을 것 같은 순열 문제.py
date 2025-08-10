for i in[*open(0)][1:]:
    N,K=map(int,i.split())
    R=range(1,N+1)
    if 1<K:print(*R)
    else:
        if N<4:print(-1)
        else:print(*R[1::2],*R[::2])
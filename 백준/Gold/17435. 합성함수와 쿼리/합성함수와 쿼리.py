[M],v,_,*l=[[*map(int,i.split())]for i in open(0)]
sp=[[i]for i in v]
i=0
for _ in[0]*20:
    for t in range(M):
        sp[t]+=sp[sp[t][-1]-1][i],
    i+=1
for m,x in l:
    i=0
    while m:
        if m%2:
            x=sp[x-1][i]
        m//=2
        i+=1
    print(x)
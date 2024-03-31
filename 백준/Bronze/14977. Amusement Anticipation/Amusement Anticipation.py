*l,=open(0)
while l:
    p,q,*l=l
    N=int(p)
    *s,=map(int,q.split())
    if N<3:print(1)
    else:
        N-=1;d=s[N]-s[N-1]
        while N!=1 and s[N-1]-s[N-2]==d:N-=1
        print(N)
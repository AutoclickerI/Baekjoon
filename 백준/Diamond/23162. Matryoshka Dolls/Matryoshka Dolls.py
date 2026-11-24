[N,Q],A,*l=[[*map(int,i.split())]for i in open(0)]

blk=200

P=[0]*(N+2)
for i,v in enumerate(A):P[v]=i
*Lk,=range(-1,N+1)
*Rk,=range(1,N+3)
r=sum(abs(P[v+1]-P[v])for v in range(N+1))

def push(v):
    global r
    a=Lk[v];b=Rk[v]
    Rk[a]=Lk[b]=v
    r+=abs(P[v]-P[a])+abs(P[b]-P[v])-abs(P[b]-P[a])

def pop(v):
    global r
    a=Lk[v];b=Rk[v]
    Rk[a]=b;Lk[b]=a
    r-=abs(P[v]-P[a])+abs(P[b]-P[v])-abs(P[b]-P[a])

L=ps=0
pe=N
d={}
for s,e in sorted(l,key=lambda i:((i[0]-1)//blk,-i[1])):
    s-=1
    if L<s//blk*blk:
        L=s//blk*blk
        while pe<N:
            push(A[pe])
            pe+=1
        while ps<L:
            pop(A[ps])
            ps+=1
    while e<pe:
        pe-=1
        pop(A[pe])
    while ps<s:
        pop(A[ps])
        ps+=1
    d[s+1,e]=r-P[Rk[0]]-P[Lk[N+1]]
    while L<ps:
        ps-=1
        push(A[ps])

for s,e in l:print(d[s,e])
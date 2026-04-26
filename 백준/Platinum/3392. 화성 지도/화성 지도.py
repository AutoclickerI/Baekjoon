[N],*l=[map(int,i.split())for i in open(0)]

q=[]
Y=[]

for x1,y1,x2,y2 in l:
    q+=(x1,y1,y2,1),(x2,y1,y2,-1)
    Y+=y1,y2

Y=sorted({*Y})
D={v:i for i,v in enumerate(Y)}
M=len(Y)-1

S=1<<M.bit_length()

t=[0]*S*2
c=[0]*S*2
L=[0]*S*2

for i in range(M):
    L[S+i]=Y[i+1]-Y[i]

for i in range(S-1,0,-1):
    L[i]=L[i<<1]+L[i<<1|1]

def pull(i):
    if c[i]:
        t[i]=L[i]
    elif i<S:
        t[i]=t[i<<1]+t[i<<1|1]
    else:
        t[i]=0

def update(l,r,v):
    l+=S
    r+=S
    a=[]

    while l<r:
        if l&1:
            c[l]+=v
            pull(l)
            a+=l,
            l+=1

        if r&1:
            r-=1
            c[r]+=v
            pull(r)
            a+=r,

        l//=2
        r//=2

    for i in a:
        i//=2
        while i:
            pull(i)
            i//=2

q.sort()

r=0
px=q[0][0]

for x,y1,y2,v in q:
    r+=t[1]*(x-px)
    update(D[y1],D[y2],v)
    px=x

print(r)
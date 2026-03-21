[Q],*l=[map(int,i.split())for i in open(0)]

N=2097152
tree=[0]*2*N

def update(i,v):
    i+=N
    tree[i]+=v
    while i:=i>>1:
        tree[i]=tree[i<<1]+tree[i<<1|1]

for q,v in l:
    if q<2:
        update(v,1)
    else:
        i=1
        while i<N:
            le=i<<1
            if v<=tree[le]:
                i=le
            else:
                v-=tree[le]
                i=le|1
        print(i-N)
        update(i-N,-1)
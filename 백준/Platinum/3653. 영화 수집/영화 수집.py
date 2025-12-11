def update(i,v):
    i+=tot
    tree[i]=v
    while 1<i:
        i//=2
        tree[i]=tree[i*2]+tree[i*2+1]

def get_val(l,r):
    l+=tot
    r+=tot
    ret=0
    while l<r:
        if l%2:
            ret+=tree[l]
            l+=1
        if r%2:
            r-=1
            ret+=tree[r]
        l//=2
        r//=2
    return ret

for _ in[0]*int(input()):
    n,m=map(int,input().split())
    *l,=map(int,input().split())
    tot=n+m
    tree=[0]*2*tot
    *idxs,=range(n)[::-1]
    for i in range(n):
        tree[tot+i]=1
    for i in range(tot-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
    for i in l:
        print(get_val(idxs[i-1]+1,tot))
        update(idxs[i-1],0)
        update(n,1)
        idxs[i-1]=n
        n+=1
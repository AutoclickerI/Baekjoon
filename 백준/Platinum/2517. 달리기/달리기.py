N,*ll=map(int,open(0))
sl=sorted(ll)
d={sl[i]+1:i for i in range(N)}
ll=[d[i+1]for i in ll]
tree=[0]*2*N

def update(i):
    i+=N
    tree[i]=1
    while 1<i:
        i//=2
        tree[i]=tree[i*2]+tree[i*2+1]

def get_val(l,r):
    l+=N;r+=N
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

for i,v in enumerate(ll,1):
    update(v)
    print(i-get_val(0,v))
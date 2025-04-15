N,M,K=map(int,input().split())

tree=[0]*2*N

for i in input().split():tree[int(i)+N-1]+=1

for i in range(N-1,0,-1):tree[i]=tree[i*2]+tree[i*2+1]

def update(idx):
    idx+=N
    tree[idx]-=1
    while 1<idx:
        idx//=2
        tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(l,r):
    l+=N
    r+=N
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

def bisect(i):
    s=i
    e=N
    while 1<e-s:
        m=s+e>>1
        if get_val(i,m):
            e=m
        else:
            s=m
    return s

for i in map(int,input().split()):
    v=bisect(i)
    update(v)
    print(v+1)
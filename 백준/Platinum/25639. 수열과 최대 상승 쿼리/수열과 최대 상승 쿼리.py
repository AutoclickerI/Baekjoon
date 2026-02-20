class node:
    def __init__(self,min=float('inf'),max=-float('inf'),up=0):
        self.min=min
        self.max=max
        self.up=up

def merge(L,R):
    return node(min(L.min,R.min),max(L.max,R.max),max(L.up,R.up,R.max-L.min))

def update(i,v):
    i+=N
    tree[i]=node(v,v)
    while 1<i:
        i//=2
        tree[i]=merge(tree[i*2],tree[i*2|1])

def getval(l,r):
    l+=N
    r+=N
    right=left=node()
    while l<r:
        if l%2:
            left=merge(left,tree[l])
            l+=1
        if r%2:
            r-=1
            right=merge(tree[r],right)
        l>>=1
        r>>=1
    return merge(left,right)
    
[N],t,_,*l=[[*map(int,i.split())]for i in open(0)]

tree=[0]*2*N
for i in range(N):
    tree[i+N]=node(t[i],t[i])

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i*2],tree[i*2|1])

for q,i,j in l:
    if q-1:
        print(getval(i-1,j).up)
    else:
        update(i-1,j)
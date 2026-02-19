class node:
    def __init__(self,max,min,AB,BC,ABC):
        self.max=max
        self.min=min
        self.AB=AB
        self.BC=BC
        self.ABC=ABC

def merge(L,R):
    return node(max(L.max,R.max),min(L.min,R.min),max(L.AB,R.AB,R.max-L.min),max(L.BC,R.BC,L.max-R.min),max(L.ABC,R.ABC,L.AB-R.min,R.BC-L.min))

def update(i,v):
    i+=N
    tree[i]=node(v,v,*[-float('inf')]*3)
    while 1<i:
        i//=2
        tree[i]=merge(tree[i*2],tree[i*2|1])

def getval(l,r):
    l+=N
    r+=N
    right=left=node(-float('inf'),float('inf'),*[-float('inf')]*3)
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
    
[N,Q],t,*l=[[*map(int,i.split())]for i in open(0)]

tree=[0]*2*N
for i in range(N):
    tree[i+N]=node(t[i],t[i],*[-float('inf')]*3)

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i*2],tree[i*2|1])

for q,i,j in l:
    if q-1:
        print(getval(i-1,j).ABC)
    else:
        update(i-1,j)
class node:
    def __init__(self,lmax=-float('inf'),rmax=-float('inf'),sum=-float('inf'),max=-float('inf')):
        self.lmax=lmax
        self.rmax=rmax
        self.sum=sum
        self.max=max

def merge(L,R):
    return node(max(L.lmax,L.sum+R.lmax),max(R.rmax,R.sum+L.rmax),L.sum+R.sum,max(L.max,R.max,L.rmax+R.lmax))

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
    tree[i+N]=node(t[i],t[i],t[i],t[i])

for i in range(N-1,0,-1):
    tree[i]=merge(tree[i*2],tree[i*2|1])

for i,j in l:
    print(getval(i-1,j).max)
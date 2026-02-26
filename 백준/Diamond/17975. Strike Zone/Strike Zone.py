import sys
input=sys.stdin.readline

class node:
    def __init__(self,lmax=0,rmax=0,sum=0,max=0):
        self.lmax=lmax
        self.rmax=rmax
        self.sum=sum
        self.max=max
    def __repr__(self):
        return f'node({self.lmax},{self.rmax},{self.sum},{self.max})'

def merge(L,R):
    return node(max(L.lmax,L.sum+R.lmax),max(R.rmax,R.sum+L.rmax),L.sum+R.sum,max(L.max,R.max,L.rmax+R.lmax))

def update(i,v):
    i+=N
    o=tree[i].sum
    tree[i]=node(o+v,o+v,o+v,o+v)
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
    return merge(left,right).max

R1=[[*map(int,input().split())]for _ in[0]*int(input())]
R2=[[*map(int,input().split())]for _ in[0]*int(input())]
s,b=map(int,input().split())
N=len(R1)+len(R2)
l=[[*i,s]for i in R1]+[[*i,-b]for i in R2]
d={v:i for i,v in enumerate(sorted({i[1]for i in l}))}
N=len(d)
l=sorted([i[0],d[i[1]],i[2]]for i in l)
t=[]
for i,j,k in l:
    if t and t[-1][0][0]==i:
        t[-1]+=(i,j,k),
    else:
        t+=[(i,j,k)],

m=-float('inf')
for i in range(len(t)):
    tree=[node()]*2*N
    for j in range(i,len(t)):
        for _,x,v in t[j]:
            update(x,v)
        m=max(m,getval(0,N))
print(m)
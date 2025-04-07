import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

class node:
    def __init__(self,n):
        self.id=n
        self.parent=0
        self.sub=[]
        self.cnt=0
    def __repr__(self):
        return f'node({self.id},{self.sub})'

N,M=map(int,input().split())

db={}
l=[]
id_db={}

for _ in[0]*N:
    p,q,r=map(int,input().split())
    l+=(p,q,r),

l.sort(key=lambda s:(-s[2],-s[1]))

llist=sorted({i[1]for i in l})

squeeze={}

for i in range(len(llist)):
    squeeze[llist[i]]=i

for p,q,r in l:
    id_db[p]=db[squeeze[q]]=node(p)

N=len(squeeze)
tree=[0]*N*2

def update(idx,val):
    idx+=N
    tree[idx]+=val
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

def bisect(val):
    s=0
    e=N
    while 1<e-s:
        m=s+e>>1
        if val<=get_val(m,N):
            s=m
        else:
            e=m
    return s

for p,q,r in l:
    v=squeeze[q]
    z=get_val(v,N)
    if z:
        i=bisect(z)
        db[v].parent=db[i]
        db[i].sub+=db[v],
    update(v,1)

def DFS(node):
    if node.sub==0:
        return 0
    for i in node.sub:
        node.cnt+=DFS(i)+1
    return node.cnt

for i in db.values():
    if i.parent==0:
        DFS(i)

for _ in[0]*M:
    n=int(input())
    print(id_db[n].parent and id_db[n].parent.id,id_db[n].cnt)
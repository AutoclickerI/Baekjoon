import sys
input=sys.stdin.readline

def update(i,v):
    i+=N
    tree[i]=v
    while i:=i>>1:
        tree[i]=tree[i<<1]+tree[i<<1|1]

def get_val(l,r):
    l+=N
    r+=N
    ret=0
    while l<r:
        if l&1:
            ret+=tree[l]
            l+=1
        if r&1:
            r-=1
            ret+=tree[r]
        l>>=1
        r>>=1
    return ret

N=int(input())
tree=[0]*N+[*map(int,input().split())]

for i in range(N-1,0,-1):
    tree[i]=tree[i<<1]+tree[i<<1|1]

Q=[]
V=[]

for _ in[0]*int(input()):
    q,*l=map(int,input().split())
    if q<2:
        V+=l,
    else:
        Q+=l,

sQ=sorted(Q)
d={}

k=0
p=0
while p<len(sQ) and sQ[p][0]==k:
    _,i,j=sQ[p]
    d[*sQ[p]]=get_val(i-1,j)
    p+=1

for i,v in V:
    k+=1
    update(i-1,v)
    while p<len(sQ) and sQ[p][0]==k:
        _,i,j=sQ[p]
        d[*sQ[p]]=get_val(i-1,j)
        p+=1

for i in Q:
    print(d[*i])
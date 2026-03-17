import sys
input=sys.stdin.readline
mod=10**9+7

def matmul(A,B):
    [a00,a01,a02,a10,a11,a12]=A
    [b00,b01,b02,b10,b11,b12]=B
    return [(a00*b00+a01*b10)%mod,
            (a00*b01+a01*b11)%mod,
            (a00*b02+a01*b12+a02)%mod,
            (a10*b00+a11*b10)%mod,
            (a10*b01+a11*b11)%mod,
            (a10*b02+a11*b12+a12)%mod]

def mat_pow(A,k):
    if k==1:
        return A
    r=mat_pow(A,k//2)
    r=matmul(r,r)
    if k&1:
        r=matmul(A,r)
    return r

def update(i,v):
    i+=N
    tree[i]=[0,0,v,1,0,0]
    while i:=i>>1:
        tree[i]=matmul(tree[i<<1|1],tree[i<<1])

def get_val(l,r):
    l+=N
    r+=N
    left=[1,0,0,0,1,0]
    right=[1,0,0,0,1,0]
    while l<r:
        if l&1:
            left=matmul(tree[l],left)
            l+=1
        if r&1:
            r-=1
            right=matmul(right,tree[r])
        l>>=1
        r>>=1
    return matmul(right,left)

N,Q=map(int,input().split())

l=[[*map(int,input().split())]for _ in[0]*Q]

idxs=sorted({0,1}|{i-2 for i,_ in l}|{i-1 for i,_ in l}|{N-1,N})
d={v:i for i,v in enumerate(idxs)}

skip=[mat_pow([1,1,0,1,0,0],j-i)for i,j in zip(idxs,idxs[1:])]

N=len(skip)

tree=[0]*N+skip

for i in range(N-1,0,-1):
    tree[i]=matmul(tree[i<<1|1],tree[i<<1])

for A,B in l:
    update(d[A-2],B)
    v00,v01,v02,v10,v11,v12=get_val(0,N)
    print((v10+v12)%mod)
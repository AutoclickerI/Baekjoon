import sys
input=sys.stdin.readline

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

def update(idx,val):
    idx+=N
    tree[idx]=val
    while 1<idx:
        idx//=2
        tree[idx]=tree[idx*2]+tree[idx*2+1]

def bisect(val):
    s=0
    e=N
    while 1<e-s:
        m=s+e>>1
        if val<=get_val(0,m):
            e=m
        else:
            s=m
    return s
    
while 1:
    N,K,M=map(int,input().split())
    if N==K==M==0:
        break
    tree=[0]*N+[1]*N
    for i in range(N-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
    
    M-=1
    
    for i in range(N-1,0,-1):
        update(M,0)
        nv=(get_val(0,M)+K-1)%i+1
        M=bisect(nv)
    
    print(bisect(1)+1)
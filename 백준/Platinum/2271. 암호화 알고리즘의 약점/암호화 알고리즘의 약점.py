import sys
input=sys.stdin.readline

def get_val_max(l,r):
    l+=N
    r+=N
    ret=0
    while l<r:
        if l%2:
            ret=max(ret,maxtree[l])
            l+=1
        if r%2:
            r-=1
            ret=max(ret,maxtree[r])
        l//=2
        r//=2
    return ret

def update(idx):
    idx+=10001
    searchtree[idx]=1
    while 1<idx:
        idx//=2
        searchtree[idx]=searchtree[idx*2]|searchtree[idx*2+1]

def search(l,r):
    l+=10001
    r+=10001
    ret=0
    while l<r:
        if l%2:
            ret|=searchtree[l]
            l+=1
        if r%2:
            r-=1
            ret|=searchtree[r]
        l//=2
        r//=2
    return ret

for _ in[0]*int(input()):
    N=int(input())
    *A,=map(int,input().split())
    maxtree=[0]*N+A
    
    for i in range(N-1,0,-1):
        maxtree[i]=max(maxtree[i*2],maxtree[i*2+1])
    
    searchtree=[0]*2*10001
    
    f=0
    
    for q in range(1,N-2):
        update(A[q-1])
        minval=maxval=A[q+1]
        for s in range(q+2,N):
            if A[q]<A[s]:
                maxval=max(maxval,A[s])
                if A[s]<maxval:
                    f|=search(A[s],maxval)
            if A[q]>A[s]:
                minval=min(minval,A[s])
                if minval<A[s]:
                    f|=search(minval,A[s])
    
    print('YNeos'[1-f::2])
import sys
input=sys.stdin.readline

N=int(input())

tree=[0]*N
tree+=map(int,input().split())

for i in range(N-1,0,-1):
    tree[i]=tree[i*2]+tree[i*2+1]

def update(idx,v):
    idx+=N
    tree[idx]+=v
    while idx:=idx//2:
        tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(l,r):
    l+=N;r+=N
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

def bisect(n):
    s=0;e=N
    while 1<e-s:
        m=s+e>>1
        if get_val(0,m)<n:
            s=m
        else:
            e=m
    return s
    

for _ in[0]*int(input()):
    q,*l=map(int,input().split())
    if q==1:
        update(l[0]-1,l[1])
    else:
        print(bisect(l[0])+1)
import sys
input=sys.stdin.readline

N=65537

tree=[0]*2*N

n,k=map(int,input().split())

l=[int(input())for _ in[0]*n]

for i in l[:k-1]:
    tree[i+N]+=1

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

a=0
for i in range(k-1,n):
    update(l[i],1)
    a+=bisect((k+1)//2)
    update(l[i-k+1],-1)
print(a)
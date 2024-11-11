import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())

tree=[0]*N+[int(input())for _ in[0]*N]
mod=10**9+7

for i in range(N-1,0,-1):
    tree[i]=tree[i*2]*tree[i*2+1]%mod

def update(target,val):
    target+=N
    tree[target]=val
    while 1<target:
        target//=2
        tree[target]=tree[target*2]*tree[target*2+1]%mod

def get_val(left,right):
    left+=N
    right+=N
    ret=1
    while left<right:
        if left%2:
            ret=ret*tree[left]%mod
            left+=1
        if right%2:
            right-=1
            ret=ret*tree[right]%mod
        right//=2
        left//=2
    return ret

for _ in[0]*(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update(b-1,c)
    else:
        print(get_val(b-1,c))
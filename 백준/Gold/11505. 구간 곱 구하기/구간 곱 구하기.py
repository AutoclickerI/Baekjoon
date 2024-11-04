import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
l=[int(input())for _ in[0]*N]
tree_size=N*4
tree=[0]*tree_size
mod=10**9+7

# [start, end)
def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
    else:
        val=build(start,(start+end)//2,idx*2)*build((start+end)//2,end,idx*2+1)%mod
        tree[idx]=val
    return tree[idx]

# [start, end) is current checkint pos. [left, right) is target pos
def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 1
    if left<=start and end<=right:
        return tree[idx]
    return get_val(start,(start+end)//2,left,right,2*idx)*get_val((start+end)//2,end,left,right,2*idx+1)%mod

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        return
    mid=(start+end)//2
    if start<=target<mid:
        update(start,mid,target,val,2*idx)
    else:
        update(mid,end,target,val,2*idx+1)
    tree[idx]=tree[2*idx]*tree[2*idx+1]%mod

build(0,N)

for _ in[0]*(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,N,b-1,c)
    else:
        print(get_val(0,N,b-1,c))
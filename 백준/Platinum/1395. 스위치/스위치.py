import sys
input=sys.stdin.readline

N,M=map(int,input().split())
tree_size=N*4
tree=[0]*tree_size
lazy=[0]*tree_size

def propagate(start,end,idx):
    if lazy[idx]:
        if 1<end-start:
            lazy[idx*2]^=1
            lazy[idx*2+1]^=1
        tree[idx]=end-start-tree[idx]
        lazy[idx]=0

# [start,end), [left,right)
def update_lazy(start,end,left,right,idx=1):
    if end<=left or right<=start:
        propagate(start,end,idx)
        return tree[idx]
    if left<=start and end<=right:
        lazy[idx]^=1
        return [tree[idx],end-start-tree[idx]][lazy[idx]]
    else:
        propagate(start,end,idx)
        if end-start==1:
            return tree[idx]
        mid=(start+end)//2
        val=update_lazy(start,mid,left,right,idx*2)+update_lazy(mid,end,left,right,idx*2+1)
        tree[idx]=val
        return tree[idx]
        
def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    else:
        mid=(start+end)//2
        return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

for _ in[0]*M:
    a,b,c=map(int,input().split())
    if a:
        print(get_val(0,N,b-1,c))
    else:
        update_lazy(0,N,b-1,c)
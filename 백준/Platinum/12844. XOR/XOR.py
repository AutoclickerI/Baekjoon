import sys
input=sys.stdin.readline

N=int(input())
*l,=map(int,input().split())
tree_size=N*4
tree=[0]*tree_size
lazy=[0]*tree_size

# [start, end)
def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
    else:
        val=build(start,(start+end)//2,idx*2)^build((start+end)//2,end,idx*2+1)
        tree[idx]=val
    return tree[idx]

def propagate(start,end,idx):
    if lazy[idx]:
        tree[idx]^=lazy[idx]*(end-start&1)
        if 1<end-start:
            lazy[idx*2]^=lazy[idx]
            lazy[idx*2+1]^=lazy[idx]
        lazy[idx]=0

# [start, end) is current checkint pos. [left, right) is target pos
def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    return get_val(start,(start+end)//2,left,right,2*idx)^get_val((start+end)//2,end,left,right,2*idx+1)

def update_lazy(start,end,left,right,val,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        lazy[idx]^=val
        return val*(end-start&1)
    else:
        mid=(start+end)//2
        up=update_lazy(start,mid,left,right,val,2*idx)^update_lazy(mid,end,left,right,val,2*idx+1)
        tree[idx]^=up
        return up

build(0,N)

for _ in[0]*int(input()):
    a,*l=map(int,input().split())
    if a==1:
        b,c,d=l
        update_lazy(0,N,b,c+1,d)
    else:
        a,b=l
        print(get_val(0,N,a,b+1))
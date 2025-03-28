import sys
input=sys.stdin.readline

N=int(input())
l=[int(input())for _ in[0]*N]
tree_size=N*4
tree=[0]*tree_size
lazy=[0]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)+build(mid,end,idx*2+1)
    return tree[idx]

def propagate(start,end,idx):
    if lazy[idx]:
        tree[idx]+=lazy[idx]*(end-start)
        if 1<end-start:
            lazy[idx*2]+=lazy[idx]
            lazy[idx*2+1]+=lazy[idx]
        lazy[idx]=0

def update_lazy(start,end,left,right,val,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return tree[idx]
    if left<=start and end<=right:
        lazy[idx]+=val
        propagate(start,end,idx)
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=update_lazy(start,mid,left,right,val,idx*2)+update_lazy(mid,end,left,right,val,idx*2+1)
    return tree[idx]

def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

build(0,N)
for _ in[0]*int(input()):
    q,i,j=input().split()
    if q=='U':
        update_lazy(0,N,int(i)-1,int(i),int(j))
    else:
        print(get_val(0,N,int(i)-1,int(j)))
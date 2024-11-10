import sys
input=sys.stdin.readline

N,T=map(int,input().split())

l=[1]*N
tree_size=N*4
tree=[0]*tree_size

# [start, end)
def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
    else:
        val=build(start,(start+end)//2,idx*2)+build((start+end)//2,end,idx*2+1)
        tree[idx]=val
    return tree[idx]

# [start, end) is current checkint pos. [left, right) is target pos
def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    return get_val(start,(start+end)//2,left,right,2*idx)+get_val((start+end)//2,end,left,right,2*idx+1)

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,2*idx)
    else:
        update(mid,end,target,val,2*idx+1)
    tree[idx]=tree[2*idx]+tree[2*idx+1]

build(0,N)

for _ in[0]*T:
    q,i,*j=input().split()
    if q=='R':
        update(0,N,int(i)-1,0)
    else:
        print(get_val(0,N,int(i)-1,int(j[0])))
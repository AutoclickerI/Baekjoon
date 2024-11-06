import sys
input=sys.stdin.readline

N=10**6

tree_size=N*4
tree=[0]*tree_size

def update(start,end,target,val,idx=1):
    if target<start or end<=target:
        return
    if end-start==1:
        tree[idx]+=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_sum(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_sum(start,mid,left,right,idx*2)+get_sum(mid,end,left,right,idx*2+1)

def bisect_left(val):
    s=0
    e=N
    while 1<e-s:
        mid=(s+e)//2
        if val<=get_sum(0,N,0,mid):
            e=mid
        else:
            s=mid
    return s

for _ in[0]*int(input()):
    q,a,*b=map(int,input().split())
    if q==1:
        idx=bisect_left(a)
        print(idx+1)
        update(0,N,idx,-1)
    else:
        update(0,N,a-1,b[0])
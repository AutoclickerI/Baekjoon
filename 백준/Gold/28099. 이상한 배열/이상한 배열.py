import sys
input=sys.stdin.readline

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=max(build(start,mid,idx*2),build(mid,end,idx*2+1))
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]+=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return max(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

for T in[0]*int(input()):
    N=int(input())
    
    tree_size=N*4
    tree=[0]*tree_size

    *l,=map(int,input().split())
    build(0,N)
    db=[[]for _ in[0]*-~N]
    for idx,i in enumerate(l):
        db[i]+=idx,
    
    f=0
    for idx,i in enumerate(db):
        for s,e in zip(i,i[1:]):
            f|=idx<get_val(0,N,s,e+1)
    print('YNeos'[f::2])
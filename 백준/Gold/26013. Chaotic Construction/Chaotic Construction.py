import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
tree_size=N*4
tree=[0]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)+build(mid,end,idx*2+1)
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if right<=start or end<=left:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

for _ in[0]*Q:
    q,a,*b=input().split()
    if q=='-':
        update(0,N,int(a)-1,1)
    elif q=='+':
        update(0,N,int(a)-1,0)
    else:
        a,b=sorted([int(a),int(b[0])])
        if get_val(0,N,a-1,b)and get_val(0,N,b-1,N)+get_val(0,N,0,a):
            print('impossible')
        else:
            print('possible')
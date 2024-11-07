import sys
input=sys.stdin.readline

N=int(input())
*l,=map(int,input().split())


tree_size=N*4
tree=[0]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=min(build(start,mid,idx*2),build(mid,end,idx*2+1))
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
    tree[idx]=min(tree[idx*2],tree[idx*2+1])

def get_val(start,end,left,right,idx=1):
    if right<=start or end<=left:
        return 9e9
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return min(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

def bisect_left(s,e):
    minval=get_val(0,N,s,e)
    while 1<e-s:
        mid=(s+e)//2
        if minval<get_val(0,N,s,mid):
            s=mid
        else:
            e=mid
    return s

build(0,N)

for _ in[0]*int(input()):
    q,*i=map(int,input().split())
    if q==1:
        update(0,N,i[0]-1,i[1])
    else:
        print(bisect_left(0,N)+1)
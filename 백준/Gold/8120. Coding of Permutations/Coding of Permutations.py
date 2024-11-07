N,*l=map(int,open(0))

tree_size=N*4
tree=[0]*tree_size
d=[1]*N

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=d[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)+build(mid,end,idx*2+1)
    return tree[idx]

def update(start,end,target,idx=1):
    if end-start==1:
        tree[idx]=0
        return
    
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,idx*2)
    else:
        update(mid,end,target,idx*2+1)
        
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

def bisect_right(val):
    s=0
    e=N+1
    while 1<e-s:
        mid=(s+e)//2
        if val<get_val(0,N,mid,N):
            s=mid
        else:
            e=mid
    return s


build(0,N)
ans=[]
f=0

while l:
    v=l.pop()
    f|=len(l)<v
    idx=bisect_right(v)
    ans+=idx+1,
    update(0,N,idx)
print(*f*['NIE']or ans[::-1])
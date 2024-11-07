import sys
input=sys.stdin.readline

N=86400
tree_size=N*4
tree=[0]*tree_size
lazy=[0]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=max(build(start,mid,idx*2),build(mid,end,idx*2+1))
    return tree[idx]

def propagate(start,end,idx):
    if lazy[idx]:
        tree[idx]+=lazy[idx]*(end-start)
        if 1<end-start:
            lazy[idx*2]+=lazy[idx]
            lazy[idx*2+1]+=lazy[idx]
        lazy[idx]=0

def update_lazy(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return tree[idx]
    if left<=start and end<=right:
        lazy[idx]+=1
        propagate(start,end,idx)
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=update_lazy(start,mid,left,right,idx*2)+update_lazy(mid,end,left,right,idx*2+1)
    return tree[idx]

def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

for _ in[0]*int(input()):
    q,a,b,c,d,e,f=map(int,input().replace(*'- ').replace(*': ').split())
    s,e=a*3600+b*60+c,3600*d+60*e+f
    if q==1:
        if e<s:
            update_lazy(0,N,s,N)
            update_lazy(0,N,0,e)
        else:
            update_lazy(0,N,s,e)
    else:
        if e<s:
            print(get_val(0,N,s,N)+get_val(0,N,0,e))
        else:
            print(get_val(0,N,s,e))
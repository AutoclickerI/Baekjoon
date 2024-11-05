import sys
input=sys.stdin.readline

MOD=10**9+7

N=int(input())
tree_size=N*4
*l,=map(int,input().split())
tree=[0]*tree_size
lazy=[[1,0]for _ in[0]*tree_size]

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=(build(start,mid,idx*2)+build(mid,end,idx*2+1))%MOD
    return tree[idx]

def propagate(start,end,idx):
    if lazy[idx]!=[1,0]:
        mul,add=lazy[idx]
        tree[idx]=(tree[idx]*mul+add*(end-start))%MOD
        if 1<end-start:
            mul_t,add_t=lazy[idx*2]
            lazy[idx*2]=[mul_t*mul%MOD,(add_t*mul+add)%MOD]
            mul_t,add_t=lazy[idx*2+1]
            lazy[idx*2+1]=[mul_t*mul%MOD,(add_t*mul+add)%MOD]
        lazy[idx]=[1,0]

def update_lazy(start,end,left,right,op,val,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return tree[idx]
    if left<=start and end<=right:
        mul,add=lazy[idx]
        if op==1:
            lazy[idx][1]=(lazy[idx][1]+val)%MOD
        elif op==2:
            lazy[idx]=[mul*val%MOD,add*val%MOD]
        elif op==3:
            lazy[idx]=[0,val]
        propagate(start,end,idx)
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=(update_lazy(start,mid,left,right,op,val,idx*2)+update_lazy(mid,end,left,right,op,val,idx*2+1))%MOD
    return tree[idx]

def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return (get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1))%MOD

build(0,N)

for _ in[0]*int(input()):
    q,x,y,*z=map(int,input().split())
    if q==4:
        print(get_val(0,N,x-1,y))
    else:
        update_lazy(0,N,x-1,y,q,z[0])
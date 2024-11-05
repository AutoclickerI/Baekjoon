import sys
input=sys.stdin.readline

N=int(input())
tree_size=N*4
tree=[0]*tree_size
lazy=[[0,0]for _ in[0]*tree_size]

*l,=map(int,input().split())

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)+build(mid,end,idx*2+1)
    return tree[idx]

def propagate(start,end,idx):
    if lazy[idx]!=[0,0]:
        p,s=lazy[idx]
        tree[idx]+=(2*p+(end-start-1)*s)*(end-start)//2
        if 1<end-start:
            lazy[idx*2][0]+=p
            lazy[idx*2][1]+=s
            lazy[idx*2+1][0]+=p+((start+end)//2-start)*s
            lazy[idx*2+1][1]+=s
        lazy[idx]=[0,0]

def update_lazy(start,end,left,right,idx=1):
    if end<=left or right<=start:
        propagate(start,end,idx)
        return tree[idx]
    if left<=start and end<=right:
        lazy[idx][0]+=start+1-left
        lazy[idx][1]+=1
        return tree[idx]+(2*lazy[idx][0]+(end-start-1)*lazy[idx][1])*(end-start)//2
    else:
        propagate(start,end,idx)
        mid=(start+end)//2
        tree[idx]=update_lazy(start,mid,left,right,idx*2)+update_lazy(mid,end,left,right,idx*2+1)
        return tree[idx]

def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    else:
        mid=(start+end)//2
        return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

build(0,N)

for _ in[0]*int(input()):
    Q,*l=map(int,input().split())
    if Q==1:
        update_lazy(0,N,l[0]-1,l[1])
    else:
        print(get_val(0,N,l[0]-1,l[0]))
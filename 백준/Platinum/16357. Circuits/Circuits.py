import sys
input=sys.stdin.readline

N=int(input())
l=[]
s=set()
for _ in[0]*N:
    _,uy,_,vy=map(int,input().split())
    l+=(vy,uy),
    s|={vy,uy}
d={j:i for i,j in enumerate(sorted(s))}

N=len(d)
tree_size=N*4
tree=[0]*tree_size
lazy=[0]*tree_size

def propagate(start,end,idx):
    if lazy[idx]:
        tree[idx]+=lazy[idx]
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
    tree[idx]=max(update_lazy(start,mid,left,right,val,idx*2),update_lazy(mid,end,left,right,val,idx*2+1))
    return tree[idx]

def get_val(start,end,left,right,idx=1):
    propagate(start,end,idx)
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    
    mid=(start+end)//2
    return max(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

l=[(d[s],d[e]+1)for s,e in l]
l.sort()
for s,e in l:
    update_lazy(0,N,s,e,1)

maxval=0
ptr=0
anslist=[get_val(0,N,i,i+1)for i in range(N)]

for i in range(1,N):
    while ptr<len(l) and l[ptr][0]<=i:
        s,e=l[ptr]
        update_lazy(0,N,s,e,-1)
        ptr+=1
    maxval=max(maxval,anslist[s]+get_val(0,N,0,N))

print(maxval)
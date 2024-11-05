MOD=10**9+7
N=int(input())
*l,=map(int,input().split())
dp=[1]*N
idx_l=sorted(range(N),key=lambda i:(l[i],-i))

tree_size=N*4

def update(start,end,ptr,val,idx=1):
    if end-start==1:
        tree[idx]=val
        return
    mid=(start+end)//2
    if ptr<mid:
        update(start,mid,ptr,val,idx*2)
    else:
        update(mid,end,ptr,val,idx*2+1)
    tree[idx]=(tree[idx*2]+tree[idx*2+1])%MOD

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=right and end<=right:
        return tree[idx]
    
    mid=(start+end)//2
    return(get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1))%MOD
    
for _ in[0]*10:
    tmp=[0]*N
    tree=[0]*tree_size
    for i in range(N):
        tmp[idx_l[i]]=get_val(0,N,0,idx_l[i])
        update(0,N,idx_l[i],dp[idx_l[i]])
    dp=tmp
print(sum(dp)%MOD)
N=int(input())
*l,=map(int,input().split())
idx_l=sorted(range(N),key=lambda i:l[i])


tree_size=N*4
tree=[0]*tree_size

def update(start,end,target,idx=1):
    if target<start or end<=target:
        return
    if end-start==1:
        tree[idx]+=1
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,idx*2)
    else:
        update(mid,end,target,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_sum(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_sum(start,mid,left,right,idx*2)+get_sum(mid,end,left,right,idx*2+1)

ans=0
for i in idx_l:
    update(0,N,i)
    ans+=get_sum(0,N,i+1,N)
print(ans)
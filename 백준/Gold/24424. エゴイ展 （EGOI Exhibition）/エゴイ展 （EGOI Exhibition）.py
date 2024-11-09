import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

tree_size=M*4
tree=[0]*tree_size
dp=[0]*M

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        dp[start]=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=max(tree[idx*2],tree[idx*2+1])

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start or start==end:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return max(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

for _ in range(N):
    a,v=map(int,input().split())
    dp_a=dp[a-1]
    update(0,M,a-1,max(v+max(get_val(0,M,0,a-1),get_val(0,M,a,M)),dp_a))
print(get_val(0,M,0,M))
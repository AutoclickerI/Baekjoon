import sys
input=sys.stdin.readline

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)+build(mid,end,idx*2+1)
    return tree[idx]

def update(start,end,target,idx=1):
    if end-start==1:
        tree[idx]=1
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,idx*2)
    else:
        update(mid,end,target,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if right<=start or end<=left:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

for T in range(int(input())):
    N=int(input())
    l=[int(input())for _ in[0]*N]
    
    tree_size=N*4
    tree=[0]*tree_size
    ans=[]
    while l:
        v=l.pop()
        if get_val(0,N,0,v):
            ans+=v,
        update(0,N,v-1)
    print(len(ans))
    for i in sorted(ans):
        print(i)
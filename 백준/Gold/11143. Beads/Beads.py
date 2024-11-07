import sys
input=sys.stdin.readline

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]+=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=tree[idx*2]+tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)+get_val(mid,end,left,right,idx*2+1)

for T in[0]*int(input()):
    B,P,Q=map(int,input().split())
    
    tree_size=B*4
    tree=[0]*tree_size
    
    for _ in[0]*(P+Q):
        q,i,j=input().split()
        if q=='P':
            update(0,B,int(i)-1,int(j))
        else:
            print(get_val(0,B,int(i)-1,int(j)))
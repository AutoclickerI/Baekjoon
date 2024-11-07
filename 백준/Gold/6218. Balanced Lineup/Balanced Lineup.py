import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
l=[int(input())for _ in[0]*N]

tree_size=N*4
tree=[(0,0)]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start],l[start]
        return tree[idx]
    mid=(start+end)//2
    (a,b),(c,d)=build(start,mid,idx*2),build(mid,end,idx*2+1)
    tree[idx]=min(a,c),max(b,d)
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val,val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    (a,b),(c,d)=tree[idx*2],tree[idx*2+1]
    tree[idx]=min(a,c),max(b,d)

def get_val(start,end,left,right,idx=1):
    if right<=start or end<=left:
        return 9e9,-9e9
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    (a,b),(c,d)=get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1)
    return min(a,c),max(b,d)

build(0,N)

for _ in[0]*Q:
    s,e=map(int,input().split())
    i,j=get_val(0,N,s-1,e)
    print(j-i)
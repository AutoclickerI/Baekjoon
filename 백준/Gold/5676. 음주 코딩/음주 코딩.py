import sys
input=sys.stdin.readline

def sign(n):
    if n<0:
        return -1
    if n>0:
        return 1
    return 0

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=build(start,mid,idx*2)*build(mid,end,idx*2+1)
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=tree[idx*2]*tree[idx*2+1]

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 1
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return get_val(start,mid,left,right,idx*2)*get_val(mid,end,left,right,idx*2+1)

try:
    while 1:
        N,K=map(int,input().split())
        *l,=map(sign,map(int,input().split()))
        
        tree_size=N*4
        tree=[1]*tree_size
        
        build(0,N)
        
        s=''
        for _ in[0]*K:
            q,i,j=input().split()
            if q=='C':
                update(0,N,int(i)-1,sign(int(j)))
            else:
                s+='0+-'[get_val(0,N,int(i)-1,int(j))]
        print(s)
except:
    0
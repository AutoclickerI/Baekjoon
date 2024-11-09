import sys
input=sys.stdin.readline

class block:
    def __init__(self,pos,size):
        self.pos=pos
        self.size=size
    def __str__(self):
        return str(self.pos)
N=100002
tree_size=N*4
tree=[0]*tree_size

l=[0]*N
l[1]=N-2

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=max(build(start,mid,idx*2),build(mid,end,idx*2+1))
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=val
        l[start]=val
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=max(tree[idx*2],tree[idx*2+1])

def get_val(start,end,left,right,idx=1):
    if end<=left or right<=start:
        return 0
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return max(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

build(0,N)

def malloc(val):
    if get_val(0,N,0,N)<val:
        return 0
    s=0
    e=N
    while 1<e-s:
        mid=(s+e)//2
        if val<=get_val(0,N,0,mid):
            e=mid
        else:
            s=mid
    segment=get_val(0,N,s,s+1)
    update(0,N,s,0)
    update(0,N,s+segment-1,0)
    update(0,N,s+val,segment-val)
    update(0,N,s+segment-1,val-segment)
    return block(s,val)

def free(val):
    if val==0:
        return 0
    pos=val.pos
    size=val.size
    if l[pos-1]<0:
        merge_check=l[pos-1]
        update(0,N,pos-1,0)
        pos+=merge_check
        size-=merge_check
    
    merge_check=l[pos+size]
    if merge_check:
        update(0,N,pos+size,0)
        size+=abs(merge_check)
    update(0,N,pos,size)
    update(0,N,pos+size-1,-size)

d={}

for _ in[0]*int(input()):
    s=input()
    if '='in s:
        d[s[:4]]=malloc(int(s[12:-3]))
    else:
        if 'free' in s:
            if s[5:9]in d:
                free(d[s[5:9]])
                del d[s[5:9]]
        else:
            if s[6:10]in d:
                print(d[s[6:10]])
            else:
                print(0)
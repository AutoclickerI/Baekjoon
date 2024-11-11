import sys
input=sys.stdin.readline

class block:
    def __init__(self,pos,size):
        self.pos=pos
        self.size=size
    def __str__(self):
        return str(self.pos)
N=100002

tree_size=2*N
tree=[0]*tree_size
tree[1+N]=N-2

for i in range(N-1,0,-1):
    tree[i]=max(tree[i*2],tree[i*2+1])

def update(target,val):
    target+=N
    tree[target]=val
    while 1<target:
        target//=2
        tree[target]=max(tree[target*2],tree[target*2+1])

def get_val(left,right):
    left+=N
    right+=N
    ret=0
    while left<right:
        if left%2:
            ret=max(ret,tree[left])
            left+=1
        if right%2:
            right-=1
            ret=max(ret,tree[right])
        left//=2
        right//=2
    return ret

def malloc(val):
    if get_val(0,N)<val:
        return 0
    s=0
    e=N
    while 1<e-s:
        mid=(s+e)//2
        if val<=get_val(0,mid):
            e=mid
        else:
            s=mid
    segment=get_val(s,s+1)
    update(s,0)
    update(s+segment-1,0)
    update(s+val,segment-val)
    update(s+segment-1,val-segment)
    return block(s,val)

def free(val):
    if val==0:
        return 0
    pos=val.pos
    size=val.size
    if tree[N+pos-1]<0:
        merge_check=tree[N+pos-1]
        update(pos-1,0)
        pos+=merge_check
        size-=merge_check
    
    merge_check=tree[N+pos+size]
    if merge_check:
        update(pos+size,0)
        size+=abs(merge_check)
    update(pos,size)
    update(pos+size-1,-size)

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
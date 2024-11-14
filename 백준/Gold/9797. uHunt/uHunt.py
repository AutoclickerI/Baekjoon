import sys
input=sys.stdin.readline

N=10000
tree_size=N*2
d={}

def update(tree,target,val):
    target+=N
    tree[target]+=val
    while 1<target:
        target//=2
        tree[target]=tree[target*2]+tree[target*2+1]

def get_val(tree,left,right):
    left+=N
    right+=N
    ret=0
    while left<right:
        if left%2:
            ret+=tree[left]
            left+=1
        if right%2:
            right-=1
            ret+=tree[right]
        left//=2
        right//=2
    return ret

for _ in[0]*int(input()):
    pid,uid,time=input().split()
    tree,dic,tree_min=d.get(pid,([0]*tree_size,{},10000))
    time_int=int(time.replace('.',''))
    time_cur=dic.get(uid,10000)
    if time_cur<=time_int:
        print('submission ignored')
    else:
        if time_cur<10000:
            update(tree,time_cur,-1)
        dic[uid]=time_int
        update(tree,time_int,1)
        tree_min=min(tree_min,time_int)
        print(pid,uid,time,f'{tree_min/1000:.3f}',get_val(tree,0,time_int+1))
    d[pid]=tree,dic,tree_min
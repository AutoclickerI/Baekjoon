N,M=map(int,input().split())

tree_size=N*2
tree=[0]*tree_size
tree[N:]=map(int,input().split())

for i in range(N-1,0,-1):
    tree[i]=tree[i*2]+tree[i*2+1]

def update(target,val):
    target+=N
    tree[target]=val
    while 1<target:
        target//=2
        tree[target]=tree[target*2]+tree[target*2+1]

def get_val(left,right):
    left+=N
    right+=N
    res=0
    while left<right:
        if left&1:
            res+=tree[left]
            left+=1
        if right&1:
            right-=1
            res+=tree[right]
        left//=2
        right//=2
    return res

for i in map(int,input().split()):
    print(get_val(0,i-1)+1)
    update(i-1,0)
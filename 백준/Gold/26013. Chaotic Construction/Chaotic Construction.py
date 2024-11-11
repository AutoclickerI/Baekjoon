import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
tree_size=N*2
tree=[0]*tree_size

def update(target,val):
    target+=N
    tree[target]=val
    while 1<target:
        target//=2
        tree[target]=tree[target*2]+tree[target*2+1]

def get_val(left,right):
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

for _ in[0]*Q:
    q,a,*b=input().split()
    if q=='-':
        update(int(a)-1,1)
    elif q=='+':
        update(int(a)-1,0)
    else:
        a,b=sorted([int(a),int(b[0])])
        if get_val(a-1,b)and get_val(b-1,N)+get_val(0,a):
            print('impossible')
        else:
            print('possible')
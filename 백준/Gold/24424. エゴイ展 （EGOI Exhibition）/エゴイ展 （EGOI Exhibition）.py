import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

tree_size=M*2
tree=[0]*tree_size

def update(target,val):
    target+=M
    tree[target]=val
    while 1<target:
        target//=2
        tree[target]=max(tree[target*2],tree[target*2+1])

def get_val(left,right):
    left+=M
    right+=M
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

for _ in range(N):
    a,v=map(int,input().split())
    dp_a=get_val(a-1,a)
    update(a-1,max(v+max(get_val(0,a-1),get_val(a,M)),dp_a))
print(get_val(0,M))
import sys
input=sys.stdin.readline

N,K=map(int,input().split())

tree=[0]*N
tree+=map(int,input().split())

for i in range(N-1,0,-1):tree[i]=tree[i*2]|tree[i*2+1]

def get_val(left,right):
    ret=0
    left+=N
    right+=N
    while left<right:
        if left%2:
            ret|=tree[left]
            left+=1
        if right%2:
            right-=1
            ret|=tree[right]
        left//=2
        right//=2
    return ret

def bisect_right(start):
    s=start+1
    e=N+1
    while 1<e-s:
        m=(s+e)//2
        if K<get_val(start,m):
            e=m
        else:
            s=m
    if get_val(start,s)==K:
        return s
    return -1

def bisect_left(start):
    s=start
    e=N
    while 1<e-s:
        m=(s+e)//2
        if K<=get_val(start,m):
            e=m
        else:
            s=m
    if get_val(start,e)==K:
        return e
    return -1

def get_interval(start):
    start_pos=bisect_left(start)
    if start_pos<0:
        return 0
    end_pos=bisect_right(start)
    return end_pos-start_pos+1

print(sum(get_interval(i)for i in range(N)))
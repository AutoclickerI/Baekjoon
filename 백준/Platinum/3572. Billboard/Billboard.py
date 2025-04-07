import sys
input=sys.stdin.readline

h,w,n=map(int,input().split())

h=min(h,200002)

tree=[0]*h*2

def update(idx,val):
    idx+=h
    tree[idx]+=val
    while 1<idx:
        idx//=2
        tree[idx]=min(tree[idx*2],tree[idx*2+1])

def get_val(l,r):
    l+=h
    r+=h
    ret=None
    while l<r:
        if l%2:
            if ret==None:
                ret=tree[l]
            else:
                ret=min(ret,tree[l])
            l+=1
        if r%2:
            r-=1
            if ret==None:
                ret=tree[r]
            else:
                ret=min(ret,tree[r])
        l//=2
        r//=2
    return ret

def bisect(val):
    s=0
    e=h
    while 1<e-s:
        m=e+s>>1
        if val<=w-get_val(0,m):
            e=m
        else:
            s=m
    return s

max_idx=1

for _ in[0]*n:
    n=int(input())
    if w-get_val(0,max_idx)<n:
        if max_idx<h and n<=w:
            update(max_idx,n)
            max_idx+=1
            print(max_idx)
        else:
            print(-1)
    else:
        idx=bisect(n)
        print(idx+1)
        update(idx,n)
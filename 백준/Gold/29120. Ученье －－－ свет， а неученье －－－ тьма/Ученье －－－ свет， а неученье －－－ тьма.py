import sys
input=sys.stdin.readline

*is_prime,=range(101)
for i in range(2,101):
    if is_prime[i]:
        is_prime[2*i::i]=[0]*len(range(2*i,101,i))
primes=[i for i in is_prime if 1<i]

def factorize(n):
    d={}
    for i in primes:
        while n%i<1:
            d[i]=d.get(i,0)+1
            n//=i
    if n-1:
        d[n]=1
    return d

def merge(a,b):
    d={**a}
    for i in b:
        d[i]=d.get(i,0)+b[i]
    return d

N=int(input())
*l,=map(factorize,map(int,input().split()))

tree_size=N*4
tree=[0]*tree_size

def build(start,end,idx=1):
    if end-start==1:
        tree[idx]=l[start]
        return tree[idx]
    mid=(start+end)//2
    tree[idx]=merge(build(start,mid,idx*2),build(mid,end,idx*2+1))
    return tree[idx]

def update(start,end,target,val,idx=1):
    if end-start==1:
        tree[idx]=factorize(val)
        return
    mid=(start+end)//2
    if target<mid:
        update(start,mid,target,val,idx*2)
    else:
        update(mid,end,target,val,idx*2+1)
    tree[idx]=merge(tree[idx*2],tree[idx*2+1])

def get_val(start,end,left,right,idx=1):
    if right<=start or end<=left:
        return {}
    if left<=start and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return merge(get_val(start,mid,left,right,idx*2),get_val(mid,end,left,right,idx*2+1))

build(0,N)
for _ in[0]*int(input()):
    q,i,j=map(int,input().split())
    if q:
        a=1
        for i in get_val(0,N,i-1,j).values():
            a=a*(i+1)%(10**9+7)
        print(a)
    else:
        update(0,N,i-1,j)
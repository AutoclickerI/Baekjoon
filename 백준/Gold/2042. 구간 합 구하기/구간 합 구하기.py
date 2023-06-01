import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
p,q,r=map(int,input().split())
l=[int(input())for _ in[0]*p]
tree=4*len(l)*[0]
n=q+r
def build(s,e,i):
    if s==e:
        tree[i]=l[s]
        return tree[i]
    m=(s+e)//2
    tree[i]=build(s,m,2*i)+build(m+1,e,2*i+1)
    return tree[i]
build(0,len(l)-1,1)
def get_sum(s,e,i,f,t):
    if e<f or t<s:
        return 0
    if f<=s and e<=t:
        return tree[i]
    m=(s+e)//2
    return get_sum(s,m,2*i,f,t)+get_sum(m+1,e,2*i+1,f,t)
def update(s,e,i,w,v):
    if w<s or w>e:
        return
    tree[i]+=v
    if s-e:
        m=(s+e)//2
        update(s,m,2*i,w,v)
        update(m+1,e,2*i+1,w,v)

while n:
    p,q,r=map(int,input().split())
    if p-1:
        print(get_sum(0,len(l)-1,1,q-1,r-1))
    else:
        update(0,len(l)-1,1,q-1,r-l[q-1])
        l[q-1]=r
    n-=1
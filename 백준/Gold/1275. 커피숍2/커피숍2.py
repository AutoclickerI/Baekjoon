import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
p,n=map(int,input().split())
*l,=map(int,input().split())
tree=4*p*[0]
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
    p,q,r,s=map(int,input().split())
    print(get_sum(0,len(l)-1,1,min(p,q)-1,max(p,q)-1))
    update(0,len(l)-1,1,r-1,s-l[r-1])
    l[r-1]=s
    n-=1
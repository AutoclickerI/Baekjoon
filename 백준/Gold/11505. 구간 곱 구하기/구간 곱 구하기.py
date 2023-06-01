import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
p,q,r=map(int,input().split())
l=[int(input())for _ in[0]*p]
tree=4*len(l)*[0]
n=q+r
M=10**9+7
def build(s,e,i):
    if s==e:
        if l[s]:
            tree[i]=[l[s],0]
        else:
            tree[i]=[1,1]
        return tree[i]
    m=(s+e)//2
    p,q=build(s,m,2*i),build(m+1,e,2*i+1)
    tree[i]=[p[0]*q[0]%M,p[1]+q[1]]
    return tree[i]
build(0,len(l)-1,1)
def get_sum(s,e,i,f,t):
    if e<f or t<s:
        return [1,0]
    if f<=s and e<=t:
        return tree[i]
    m=(s+e)//2
    p,q=get_sum(s,m,2*i,f,t),get_sum(m+1,e,2*i+1,f,t)
    return [p[0]*q[0]%M,p[1]+q[1]]
def update(s,e,i,w,v1,v2):
    if w<s or w>e:
        return
    if v1:
        if v2:
            tree[i][0]=pow(v1,-1,M)*tree[i][0]*v2%M
        else:
            tree[i][0]=pow(v1,-1,M)*tree[i][0]%M
            tree[i][1]+=1
    else:
        if v2:
            tree[i][0]=tree[i][0]*v2%M
            tree[i][1]=max(0,tree[i][1]-1)
    if s-e:
        m=(s+e)//2
        update(s,m,2*i,w,v1,v2)
        update(m+1,e,2*i+1,w,v1,v2)

while n:
    p,q,r=map(int,input().split())
    if p-1:
        a=get_sum(0,len(l)-1,1,q-1,r-1)
        print(0 if a[1]else a[0])
    else:
        update(0,len(l)-1,1,q-1,l[q-1],r)
        l[q-1]=r
    n-=1
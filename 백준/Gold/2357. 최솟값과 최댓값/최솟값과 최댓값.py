import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
def build(s,e,i):
    if s==e:
        tree[i]=[s,s]
        return tree[i]
    m=(s+e)//2
    p,q=build(s,m,2*i),build(m+1,e,2*i+1)
    tree[i]=[p[0] if l[p[0]]<l[q[0]] else q[0],p[1] if l[p[1]]>l[q[1]] else q[1]]
    return tree[i]
def get(s,e,i,f,t):
    if e<f or t<s:
        return [-1,-2]
    if f<=s and e<=t:
        return tree[i]
    m=(s+e)//2
    p,q=get(s,m,2*i,f,t),get(m+1,e,2*i+1,f,t)
    return [p[0] if l[p[0]]<l[q[0]] else q[0],p[1] if l[p[1]]>l[q[1]] else q[1]]
p,q=map(int,input().split())
l=[int(input())for _ in[0]*p]
tree=[-1]*len(l)*4
build(0,len(l)-1,1)
l+=[-2e99,2e99]
for _ in[0]*q:
    p,q=map(int,input().split())
    a=get(0,len(l)-3,1,p-1,q-1)
    print(l[a[0]],l[a[1]])
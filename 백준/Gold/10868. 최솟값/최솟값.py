import sys
sys.setrecursionlimit(9**9)
input=sys.stdin.readline
def build(s,e,i):
    if s==e:
        tree[i]=s
        return s
    m=(s+e)//2
    p,q=build(s,m,2*i),build(m+1,e,2*i+1)
    tree[i]=p if l[p]<l[q] else q
    return tree[i]
def get(s,e,i,f,t):
    if e<f or t<s:
        return -1
    if f<=s and e<=t:
        return tree[i]
    m=(s+e)//2
    p,q=get(s,m,2*i,f,t),get(m+1,e,2*i+1,f,t)
    return p if l[p]<l[q] else q
p,q=map(int,input().split())
l=[int(input())for _ in[0]*p]
tree=[-1]*len(l)*4
build(0,len(l)-1,1)
l+=[2e99]
for _ in[0]*q:
    p,q=map(int,input().split())
    print(l[get(0,len(l)-2,1,p-1,q-1)])
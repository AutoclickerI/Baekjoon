import sys
sys.setrecursionlimit(10**5)
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
def area(s,e):
    if s==e:return l[s]
    m=get(0,len(l)-2,1,s,e)
    v1=area(s,m-1)if s-m else 0
    v2=area(m+1,e)if m-e else 0
    ans=max(v1,v2,l[m]*(e-s+1))
    return ans
while(s:=input())!='0\n':
    p,*l=map(int,s.split())
    tree=4*len(l)*[-1]
    build(0,len(l)-1,1)
    tree[-1]=len(l)
    l+=[2e9]
    print(area(0,len(l)-2))
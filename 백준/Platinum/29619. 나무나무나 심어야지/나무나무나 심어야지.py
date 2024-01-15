# Not my code
# https://codeforces.com/contest/1006/submission/118525767
 
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py
from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc
 
import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**5)
 
N,M=map(int,input().split())
fruit=[0]*(N+M+1)
descendant=[[]for _ in range(N+M+1)]
*initparent,=map(int,input().split())
*initfruit,=map(int,input().split())
order=-1
 
for i in range(1,N):
    descendant[initparent[i]]+=i+1,
 
Query=[]
for _ in range(M):
    *Q,=map(int,input().split())
    if Q[0]==1:
        descendant[Q[1]]+=Q[2],
    Query+=Q,
 
segdict=[(0,0)]*(N+M+1)
 
@bootstrap
def DFS(n):
    global order
    order+=1
    tmp=order
    for i in descendant[n]:
        yield DFS(i)
    segdict[n]=tmp,order
    yield
DFS(1)
 
for i,w in enumerate(initfruit):
    fruit[segdict[i+1][0]]=w
    
tree=4*(N+M+1)*[0]
 
def build(s,e,i):
    if s==e:
        tree[i]=fruit[s]
        return tree[i]
    m=(s+e)//2
    tree[i]=build(s,m,2*i)+build(m+1,e,2*i+1)
    return tree[i]
build(0,N+M,1)
 
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
 
for Q in Query:
    if Q[0]==1:
        update(0,N+M,1,segdict[Q[2]][0],Q[3])
    else:
        print(get_sum(0,N+M,1,*segdict[Q[1]])or -1)
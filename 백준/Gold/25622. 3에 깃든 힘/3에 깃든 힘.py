import sys
sys.setrecursionlimit(10**5)
n,*Z=open(0)
n=int(n)
l=[0]+[[]for _ in[0]*n]
for i in Z:p,q=map(int,i.split());l[p]+=[q];l[q]+=[p]
heap={i:[] for i in range(n+1)}
v=[0]*(n+1)
tree1=[0]*(n+1)
tree2=[[]for _ in[0]*(n+1)]
def DFS(n,d):
    for i in l[n]:
        if~-v[i]:heap[d]+=[i];tree1[i]=n;tree2[n]+=[i];v[i]=1;DFS(i,d+1)
v[1]=1
DFS(1,0)
flag=1
ans=[]
for i in range(n,-1,-1):
    for p in heap[i]:
        if v[p]:
            v[p]=0;q=tree1[p]
            if~-v[q]:flag=0;break
            v[q]=0
            for r in tree2[q]:
                if v[r]:v[r]=0;break
            else:
                r=tree1[q]
                if~-v[r]:flag=0;break
                v[r]=0
            ans+=[(p,q,r)]
if flag:
    print('S')
    for i in ans:print(*i)
else:print('U')
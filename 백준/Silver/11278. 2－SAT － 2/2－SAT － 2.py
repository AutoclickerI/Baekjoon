import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**6)

N,M=map(int,input().split())
edges=[[]for _ in[0]*2*N]
def convert_node(n):return abs(n)*2-2+(n<0)

for _ in[0]*M:
    s,e=map(convert_node,map(int,input().split()))
    edges[e^1]+=s,
    edges[s^1]+=e,

stack=[]
res=[]

order=[0]*2*N
finished=[0]*2*N
cnt=0
def scc(n):
    global cnt
    cnt+=1
    low=order[n]=cnt
    stack.append(n)
    for e in edges[n]:
        if order[e]<1:
            low=min(low,scc(e))
        elif finished[e]<1:
            low=min(low,order[e])
    if low==order[n]:
        c=[]
        v=-1
        while n!=v:
            v=stack.pop()
            c+=v,
            finished[v]=1
        res.append(c)
    return low

for i in range(2*N):
    if finished[i]<1:
        scc(i)

scc_num=[0]*2*N

for i,t in enumerate(res):
    for v in t:
        scc_num[v]=i

ans=[-1]*N
for i in range(N):
    v=i*2
    nv=i*2+1
    if scc_num[v]==scc_num[nv]:
        exit(print(0))
    ans[i]=+(scc_num[v]<scc_num[nv])
print(1)
print(*ans)
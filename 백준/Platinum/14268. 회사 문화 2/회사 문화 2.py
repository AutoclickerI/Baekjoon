import sys
sys.setrecursionlimit(2*10**5)

[N,M],P,*l=[[*map(int,i.split())]for i in open(0)]
edges=[[]for _ in[0]*-~N]

for i,v in enumerate(P[1:],2):
    edges[v]+=i,

s=[0]*-~N
e=[0]*-~N
c=0

def DFS(n):
    global c
    s[n]=c
    c+=1
    for i in edges[n]:
        DFS(i)
    e[n]=c

DFS(1)
tree=[0]*N*2

def update(l,r,v):
    l+=N
    r+=N
    while l<r:
        if l&1:
            tree[l]+=v
            l+=1
        if r&1:
            r-=1
            tree[r]+=v
        l//=2
        r//=2

def get_val(i):
    i+=N
    r=0
    while i:
        r+=tree[i]
        i//=2
    return r

for q,i,*j in l:
    if q<2:
        update(s[i],e[i],*j)
    else:
        print(get_val(s[i]))
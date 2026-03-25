l=[0]*2+[*map(int,[*open(0)][1].split())]
v=[0]*len(l)
def DFS(n,c):
    if len(l)<=n:
        return c
    v[n]=max(DFS(n<<1,c+l[n]),DFS(n<<1|1,c+l[n]))
    return v[n]

x=DFS(1,0)

v=[x-i for i in v[len(v)//2:]]

r=0
for i,j in zip(*[iter(v)]*2):
    Mi=max(i,j)
    mi=min(i,j)
    v+=mi,
    r+=Mi-mi
print(r+sum(l))
[N],*b=[[*map(int,i.split())]for i in open(0)]

l=[]
for y in range(N):
    for x in range(N):
        if b[y][x]:l+=(b[y][x],y,x),
l.sort()

v=[N*[float('inf')]for _ in[0]*N]
for i in range(N):v[i][i]=0

def FW():
    for m in range(N):
        for s in range(N):
            for e in range(N):
                v[s][e]=min(v[s][e],v[s][m]+v[m][e])
    return v

r=0
for c,y,x in l:
    if c<v[y][x]:
        r+=c
        v[y][x]=v[x][y]=c
        FW()
print(-(b!=v)or r)
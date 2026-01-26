N,M,*l=map(int,open(0).read().split())
d=[[0]+49*[float('inf')]for _ in[0]*5]
v=[1]*N
for i in l:v[i-1]=0
for i in v:
    if i:
        t=50*[float('inf')]
        for j in range(50):
            t[j]=min(t[j],d[-1][j]+10000)
        for j in range(3,50):
            t[j-3]=min(t[j-3],d[-1][j])
        for j in range(1,50):
            t[j]=min(t[j],d[-3][j-1]+25000)
        for j in range(2,50):
            t[j]=min(t[j],d[-5][j-2]+37000)
        d+=t,
        
    else:
        d+=d[-1],

print(min(d[-1]))
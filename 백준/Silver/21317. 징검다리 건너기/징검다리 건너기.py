[N],*l,[K]=[[*map(int,i.split())]for i in open(0)]
v=[2*[float('inf')]for _ in[0]*N]
v[0]=[0,0]

for i in range(N):
    if i+1<N:
        v[i+1][0]=min(v[i+1][0],v[i][0]+l[i][0])
        v[i+1][1]=min(v[i+1][1],v[i][1]+l[i][0])
    if i+2<N:
        v[i+2][0]=min(v[i+2][0],v[i][0]+l[i][1])
        v[i+2][1]=min(v[i+2][1],v[i][1]+l[i][1])
    if i+3<N:
        v[i+3][1]=min(v[i+3][1],v[i][0]+K)

print(min(v[-1]))
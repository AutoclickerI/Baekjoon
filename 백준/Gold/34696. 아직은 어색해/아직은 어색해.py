[N,M],*l,[n]=[[*map(int,i.split())]for i in open(0)]
v=[0]*M
v[n-1]=1
xx=[l[n-1]]
y,x=l[n-1]
dists=[(y-i)**2+(x-j)**2 for i,j in l]
print(n)
for i in range(1,N):
    m=0
    for z in range(M):
        if v[z]<1 and m<dists[z]:
            m=dists[z]
            a=z
    xx+=l[a],
    v[a]=1
    print(a+1)
    yv,xv=l[a]
    for i in range(M):
        y,x=l[i]
        dists[i]=min(dists[i],(yv-y)**2+(xv-x)**2)
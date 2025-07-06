f=[0,0]
[N],*l=[[*map(int,i.split())]for i in open(0)]
for y in range(N):
    for x in range(N):
        f[y+x&1]|=l[y][x]==1
        if l[y][x]==2:z=y+x&1
if f[z]<1:print('Lena')
else:print('Kiriya')
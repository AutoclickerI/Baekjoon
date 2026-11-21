[N],*l=[[*map(int,i.split())]for i in open(0)]
r=0
m=0
def dist(i,j):
    return abs(j[0]-i[0])+abs(j[1]-i[1])
for i,j in zip(l,l[1:]):
    r+=dist(i,j)
for i,j,k in zip(l,l[1:],l[2:]):
    m=max(m,dist(i,j)+dist(j,k)-dist(i,k))
print(r-m)
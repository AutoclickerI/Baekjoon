[R,C,Q],*l=[map(int,i.split())for i in open(0)]
p=[[0]*-~C]
for i in l[:R]:
    t=[0]
    for j,v in enumerate(i):
        t+=t[-1]+p[-1][j+1]-p[-1][j]+v,
    p+=t,
for r1,c1,r2,c2 in l[R:]:
    print((p[r2][c2]-p[r2][c1-1]-p[r1-1][c2]+p[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))